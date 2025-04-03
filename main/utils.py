from django.shortcuts import get_object_or_404
from main.models import Course, Cart, CartItem


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