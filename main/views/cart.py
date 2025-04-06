from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse

from main.utils import add_to_cart, remove_from_cart, add_one_course_to_cart


@login_required
def add_to_cart_view(request, course_slug):
    """Add a product to the cart."""
    add_to_cart(request.user, course_slug)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def remove_from_cart_view(request, course_slug):
    """Remove a product from the cart."""
    remove_from_cart(request.user, course_slug)
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def join_course_view(request, course_slug):
    add_one_course_to_cart(request.user, course_slug)
    return redirect(reverse('payment_page')+'?perform_postback=true')