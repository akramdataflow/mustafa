import hashlib
import hmac

from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.conf import settings
from main.serializers import PaymentLogSerializer


class PaymentWebhookAPIView(APIView):
    """
    {
      "requestId": "036f3e12-bbde-4adf-a3c5-007b816c656f",
      "paymentId": "7a20381c-8737-4a02-a7ed-201c7390cf83",
      "status": "SUCCESS",
      "canceled": false,
      "amount": 225000,
      "confirmedAmount": 225000,
      "currency": "IQD",
      "paymentType": "CARD",
      "creationDate": "2025-01-28T23:34:29",
      "details": {
        "resultCode": "00",
        "rrn": "502800008882",
        "authId": "123456",
        "authDate": "2025-01-28T23:34:56",
        "maskedPan": "521372******8582",
        "paymentSystem": "MASTER_CARD"
      },
      "withoutAuthenticate": false,
      "additionalInfo": {}
    }
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = PaymentLogSerializer
    def post(self, request, *args, **kwargs):
        if settings.USE_SIGNATURE_VERIFICATION:
            secret_key = settings.PAYMENT_WEBHOOK_SECRET
            signature = request.headers.get('X-Signature', '')
            payload = request.body

            expected_signature = hmac.new(
                key=secret_key.encode('utf-8'),
                msg=payload,
                digestmod=hashlib.sha256
            ).hexdigest()

            if not hmac.compare_digest(expected_signature, signature):
                return Response({"error": "Invalid signature"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
