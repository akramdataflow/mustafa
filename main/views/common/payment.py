import decimal
import json
import uuid

import requests
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from main.utils import get_user_cart, get_basic_auth, get_request_header
from main.models import CartItem, Order, OrderItem, Student


@login_required
def payment_page(request):
    """Handle the payment process."""
    cart = get_user_cart(request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.quantity * item.course.get_total_price() for item in cart_items)
    billing_info = Student.objects.select_related('user').get(user=request.user)

    if request.method == 'POST' or request.GET.get('perform_postback') == 'true':
        data = {
            "requestId": str(uuid.uuid4()),
            # only customer will pay 30% of total_price as client requested
            "amount": float(total_price * decimal.Decimal(0.3)),
            "currency": "IQD",
            "locale": "en_US",
            "finishPaymentUrl": settings.PAYMENT_FINISH_URL,
            "notificationUrl": settings.PAYMENT_NOTIFICATION_URL,
            "customerInfo": {
                "firstName": request.user.first_name,
                "middleName": "",
                "lastName": request.user.last_name,
                "phone": billing_info.phone_number,
                "email": request.user.email,
                "accountId": request.user.id,
                "accountNumber": request.user.id,
                "address": billing_info.address,
                "city": billing_info.city,
                "provinceCode": billing_info.province_code,
                "postalCode": billing_info.postal_code,
                "countryCode": billing_info.country_code,
                "birthDate": billing_info.birth_date.strftime('%m%d%Y') if billing_info.birth_date else None,
                "identificationType": billing_info.identification_type,
                "identificationNumber": billing_info.identification_number,
                "identificationCountryCode": billing_info.identification_country_code,
                "identificationExpirationDate": billing_info.identification_expiration_date.strftime('%m%d%Y')
                if billing_info.identification_expiration_date else None,
                "nationality": billing_info.nationality,
                "countryOfBirth": billing_info.country_of_birth,
            }
        }

        if settings.PAYMENT_GATEWAY_PROD:
            data.pop("finishPaymentUrl")
            data.pop("notificationUrl")

        try:
            response = requests.post(
                f"{settings.PAYMENT_GATEWAY_URL}/api/v1/payment",
                headers=get_request_header(),
                data=json.dumps(data),
                auth=get_basic_auth()
            )
            response.raise_for_status()
            payment_data = response.json()
            return redirect(payment_data.get("formUrl"))
        except requests.exceptions.RequestException as e:
            messages.error(request, "Payment request failed: " + str(e))
            return redirect(reverse('payment_status'))

    context = {'cart_items': cart_items, 'total_price': total_price}
    return render(request, 'common/payment_page.html', context)


@login_required
def payment_status(request):
    """Handle successful payment and create an order."""
    status = request.GET.get("status")
    payment_id = request.GET.get("paymentId")
    request_id = request.GET.get("requestId")

    if status == "SUCCESS":
        cart = get_user_cart(request.user)
        cart_items = cart.items.all()
        total_price = sum(item.get_total_price() for item in cart_items)

        order = Order.objects.create(
            user_id=request.user.id,
            total_price=total_price,
            status=status,
            payment_id=payment_id,
            request_id=request_id,
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                course=item.course,
                quantity=item.quantity,
                price=item.get_total_price(),
                currency=item.course.currency
            )

        cart.items.all().delete()

        messages.success(request, "Payment successful! Your order has been placed.")
        return render(request, 'common/success.html', {})
    else:
        messages.warning(request, "Payment was canceled.")
        return render(request, 'common/cancel.html', {})
