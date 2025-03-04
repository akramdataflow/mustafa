from django.utils.translation import gettext_lazy as _
from django.db import models
from django.conf import settings
from core.models import TimeStampedModel


class EnrolledCourse(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Student'), on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'course')