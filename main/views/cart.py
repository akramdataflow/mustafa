from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

from main.utils import get_user_cart, add_to_cart, remove_from_cart


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