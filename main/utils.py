from typing import Tuple
import uuid
import requests

from django.conf import settings
from django.shortcuts import get_object_or_404
from requests.auth import HTTPBasicAuth
from main.models import Course, Cart, CartItem, Order


def get_user_cart(user) -> Cart:
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart

def add_to_cart(user, course_slug) -> CartItem:
    cart = get_user_cart(user)
    course = get_object_or_404(Course, slug=course_slug)
    cart_item, _ = CartItem.objects.get_or_create(cart=cart, course=course)
    return cart_item

def remove_from_cart(user, course_slug) -> Cart:
    cart = get_user_cart(user)
    course = get_object_or_404(Course, slug=course_slug)
    cart_item = get_object_or_404(CartItem, cart=cart, course=course)
    cart_item.delete() 
    return cart


def add_one_course_to_cart(user, course_slug) -> CartItem:
    cart = get_user_cart(user)
    course = get_object_or_404(Course, slug=course_slug)
    CartItem.objects.filter(cart=cart).delete()
    cart_item = CartItem.objects.create(cart=cart, course=course)
    cart_item.save()
    return cart_item

def get_request_header() -> dict:
    return {
        'X-Terminal-Id': settings.PAYMENT_GATEWAY_TERMINAL_ID,
        "Content-Type": "application/json",
    }

def get_basic_auth():
    username = settings.PAYMENT_GATEWAY_USERNAME
    password = settings.PAYMENT_GATEWAY_PASSWORD
    return HTTPBasicAuth(username, password)

class OrderOperation:
    base_url = settings.PAYMENT_GATEWAY_URL

    def refund(self, order: Order) -> Tuple[dict, bool]:
        url = f'{self.base_url}/api/v1/payment/{order.payment_id}/refund'
        data = {
            "requestId": str(uuid.uuid4()),
            "amount": order.total_price,
            "message": "Refund Order",
        }
        response = requests.post(url, json=data, headers=get_request_header(), auth=get_basic_auth())
        return response.json(), response.status_code == 200

    def cancel(self, order: Order) -> Tuple[dict, bool]:
        url = f'{self.base_url}/api/v1/payment/{order.payment_id}/cancel'
        data = {
            "requestId": str(uuid.uuid4()),
            "amount": order.total_price,
        }
        response = requests.post(url, json=data, headers=get_request_header(), auth=get_basic_auth())
        return response.json(), response.status_code == 200
