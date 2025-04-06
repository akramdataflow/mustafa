from django.db import models


class PaymentLog(models.Model):
    STATUS = (
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('AUTHENTICATION_FAILED', 'Authentication Failed'),
        ('PENDING', 'Pending'),
    )

    class Meta:
        verbose_name = "Payment Log"
        verbose_name_plural = "Payment Logs"

    payment_id = models.CharField(max_length=255)
    request_id = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS)
    canceled = models.BooleanField(default=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    confirmed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    payment_type = models.CharField(max_length=20)
    creation_date = models.DateTimeField(auto_now_add=True)
    details = models.JSONField()
    without_authenticate = models.BooleanField(default=False)
    payload = models.JSONField(default=dict)

    def __str__(self):
        return f"Payment Log: {self.payment_id} - {self.status}"
