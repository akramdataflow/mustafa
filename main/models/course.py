import uuid
import random
import string
import math

from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel, UniqueIdentifierModel
from django.db.models.signals import pre_save
from django.dispatch import receiver

from autoslug import AutoSlugField


def image_upload(instance, filename):
    imagename, extension = filename.split('.')
    return f"course/{uuid.uuid4().hex}_{imagename}.{extension}"

def course_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

class Course(TimeStampedModel, UniqueIdentifierModel):
    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')

    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    EXPERT = 'All Level'

    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
        (EXPERT, 'All Level'),
    ]

    name = models.CharField(_('Name'), max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    code = models.CharField(_('Course Code'), unique=True, default=course_code_generator, max_length=100)
    body = models.TextField(_("About"))
    image = models.ImageField(upload_to=image_upload)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='categories')
    price = models.DecimalField(_("Price"), max_digits=10, decimal_places=2)
    currency = models.ForeignKey('core.Currency', on_delete=models.SET_NULL, null=True, related_name='currencies')
    teachers = models.ManyToManyField('Teacher', related_name='teachers')
    level = models.CharField(_("Level"), max_length=20,choices=LEVEL_CHOICES, default=BEGINNER)
    lessons_count = models.IntegerField(default=0)
    requirements = models.TextField()

    discount = models.PositiveIntegerField(_('Discount Percentage'), default=0)
    discount_starts_at = models.DateField(_("Discount Starts At"), null=True)
    discount_ends_at = models.DateField(_("Discount Ends At"), null=True)

    is_active = models.BooleanField(_('Is Active'), default=True)
    has_certificate = models.BooleanField(_('Has Certificate'), default=False)

    def __str__(self):
        return self.name
    
    def has_discount(self) -> bool:
        today = timezone.now().date()
        return self.discount_starts_at <= today <= self.discount_ends_at
    
    @property
    def duration(self) -> int:
        duration = 0
        for lesson in self.lessons.all():
            duration += lesson.duration
        return duration
    
    def duration_format(self) -> str:
        minutes = math.floor(self.duration / 60)
        seconds = self.duration % 60
        hours = math.floor(minutes / 60)
        return f'{hours}:{minutes:02d}:{seconds:02d}' if hours > 0 else f'{minutes}:{seconds:02d}'
    

@receiver(pre_save, sender=Course)
def set_default_values(sender, instance, **kwargs):
    from .lesson import Lesson
    from .category import Category
    instance.category = Category.objects.filter(slug='development').first()
    instance.lessons_count = Lesson.objects.filter(course=instance).count()
    instance.save()