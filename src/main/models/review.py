from django.db import models
from django.conf import settings

from core.models import TimeStampedModel


class Review(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    body = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        unique_together = ('user', 'course')

    def __str__(self):
        return self.body