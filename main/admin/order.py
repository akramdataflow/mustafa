from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import redirect
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from main.models import OrderItem, Order
from main.utils import OrderOperation


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ('user', 'total_price', 'status', 'created_at', 'refund_order_link')
    list_filter = ('user', 'status', 'created_at',)
    search_fields = ('user__get_full_name', 'total_price')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

    def refund_order_link(self, obj):
        """Creates a refund button for eligible orders in the changelist."""
        if obj.payment_rollback_available():
            url = reverse('admin:order_refund', args=[obj.id])
            return format_html('<a class="button" href="{}">Refund</a>', url)
        return "-"

    refund_order_link.short_description = "Refund Order"
    refund_order_link.allow_tags = True

    def cancel_order_link(self, obj):
        """Creates a cancel button for eligible orders in the changelist."""
        if obj.payment_rollback_available():
            url = reverse('admin:order_cancel', args=[obj.id])
            return format_html('<a class="button" href="{}">Cancel</a>', url)
        return "-"

    cancel_order_link.short_description = "Cancel Order"
    cancel_order_link.allow_tags = True

    def get_urls(self):
        """Adds a custom URL for handling refunds."""
        urls = super().get_urls()
        custom_urls = [
            path('refund/<int:order_id>/', self.admin_site.admin_view(self.process_refund), name='order_refund'),
            path('cancel/<int:order_id>/', self.admin_site.admin_view(self.process_cancel), name='order_cancel'),
        ]
        return custom_urls + urls

    def process_refund(self, request, order_id):
        """Handles the refund logic when the button is clicked."""
        order = Order.objects.filter(id=order_id).first()
        if not order:
            self.message_user(request, _("Order not found."), messages.ERROR)
            return redirect(request.META.get('HTTP_REFERER', 'admin:main_order_changelist'))

        response, is_success = OrderOperation().refund(order)
        if is_success:
            order.status = Order.REFUNDED
            order.save()
            self.message_user(request, _("Order refunded successfully."), messages.SUCCESS)
        else:
            self.message_user(request, _("Failed to refund order."), messages.ERROR)

        return redirect(request.META.get('HTTP_REFERER', 'admin:main_order_changelist'))

    def process_cancel(self, request, order_id):
        order = Order.objects.filter(id=order_id).first()
        if not order:
            self.message_user(request, _("Order not found."), messages.ERROR)
            return redirect(request.META.get('HTTP_REFERER', 'admin:main_order_changelist'))

        response, is_success = OrderOperation().cancel(order)
        if is_success:
            order.status = Order.CANCELLED
            order.save()
            self.message_user(request, _("Order cancelled successfully."), messages.SUCCESS)
        else:
            self.message_user(request, _("Failed to cancel order."), messages.ERROR)

        return redirect(request.META.get('HTTP_REFERER', 'admin:main_order_changelist'))
