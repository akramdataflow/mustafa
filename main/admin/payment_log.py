from django.contrib import admin

from main.models import PaymentLog


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    list_display = ('payment_id', 'request_id', 'status', 'amount', 'creation_date')
    list_filter = ('status', 'creation_date')
    search_fields = ('payment_id', 'request_id')
    readonly_fields = ('payment_id', 'request_id', 'status', 'amount', 'creation_date', 'details',
                       'without_authenticate', 'payload', 'confirmed_amount', 'currency', 'payment_type', 'canceled')
    ordering = ('-creation_date',)
