from django.conf import settings
from rest_framework import serializers

from main.models import PaymentLog

class PaymentLogSerializer(serializers.Serializer):
    paymentId = serializers.UUIDField()
    requestId = serializers.UUIDField()
    status = serializers.CharField(default="PENDING")
    canceled = serializers.BooleanField(default=False)
    amount = serializers.FloatField()
    confirmedAmount = serializers.FloatField()
    currency = serializers.CharField(max_length=3)
    paymentType = serializers.CharField(max_length=24)
    creationDate = serializers.DateTimeField()
    details = serializers.JSONField()
    withoutAuthenticate = serializers.BooleanField(default=False)
    additionalInfo = serializers.JSONField()

    def save(self, **kwargs):
        PaymentLog.objects.create(
            payment_id=self.data.get("paymentId"),
            request_id=self.data.get("requestId"),
            status=self.data.get("status"),
            canceled=self.data.get("canceled"),
            amount=self.data.get("amount"),
            confirmed_amount=self.data.get("confirmedAmount"),
            currency=self.data.get("currency"),
            payment_type=self.data.get("paymentType"),
            creation_date=self.data.get("creationDate"),
            details=self.data.get("details"),
            without_authenticate=self.data.get("withoutAuthenticate"),
            payload=self.data,
        )