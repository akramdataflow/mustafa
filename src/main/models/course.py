import uuid

from django.db import models
from django.utils import timezone
from core.models import TimeStampedModel, UniqueIdentifierModel

from autoslug import AutoSlugField


def image_upload(instance, filename):
    imagename, extension = filename.split('.')
    return f"course/{uuid.uuid4().hex}_{imagename}.{extension}"

class Course(TimeStampedModel, UniqueIdentifierModel):
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

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

    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to=image_upload)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='categories')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    teachers = models.ManyToManyField('Teacher', related_name='teachers')
    level = models.CharField(max_length=20,choices=LEVEL_CHOICES, default=BEGINNER)
    lessons_count = models.IntegerField(default=0)
    requirements = models.TextField()

    discount = models.PositiveIntegerField(verbose_name='Discount Percentage', default=0)
    discount_starts_at = models.DateField()
    discount_ends_at = models.DateField()

    def __str__(self):
        return self.name
    
    def has_discount(self) -> bool:
        today = timezone.now().date()
        return self.discount_starts_at <= today <= self.discount_ends_at
    

class Lesson(TimeStampedModel, UniqueIdentifierModel):
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='name', unique=True)
    body = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='lessons/', blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_preview = models.BooleanField(default=False)

    def __str__(self):
        return self.name