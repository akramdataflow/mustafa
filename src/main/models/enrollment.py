from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class EnrolledCourse(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Student'), on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.ForeignKey('core.Currency', on_delete=models.SET_NULL, null=True, related_name='enrollments')
    is_active = models.BooleanField(default=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'course')