import decimal

from django.conf import settings
from django.db import models

from core.models import Currency
from .course import Course


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart - {self.user}"
    
    def get_total_price(self) -> decimal.Decimal:
        return sum(item.get_total_price() for item in self.items.all())
    
    def get_currency(self) -> Currency:
        return self.items.first().course.currency if self.items.exists() else None
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"CartItem - {self.cart} - {self.course}"
    
    def get_total_price(self) -> decimal.Decimal:
        return self.course.get_total_price()
    