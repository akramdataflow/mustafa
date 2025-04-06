from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class OrderManager(models.Manager):
    def queryset(self):
        return super().get_queryset().select_related('user').prefetch_related('items')


class Order(models.Model):
    objects = OrderManager()
    CANCELLED = "CANCELLED"
    REFUNDED = "REFUNDED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    STATUSES = (
        (PENDING, _('Pending')),
        (SUCCESS, _('Success')),
        (FAILED, _('Failed')),
        # After payment
        (CANCELLED, _('Cancelled')),
        (REFUNDED, _('Refunded')),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUSES, default=PENDING)

    def order_items(self):
        return self.items.all()
    
    def payment_rollback_available(self) -> bool:
        return all([self.payment_id, self.status in [self.SUCCESS, self.FAILED], self.created_at.date() == timezone.now().date()])

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    course = models.ForeignKey('main.Course', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.ForeignKey('core.Currency', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.course} in order {self.order.user.username}"
