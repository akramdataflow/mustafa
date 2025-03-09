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
    currency = models.ForeignKey('core.Currency', on_delete=models.SET_NULL, null=True, related_name='currencies')
    teachers = models.ManyToManyField('Teacher', related_name='teachers')
    level = models.CharField(max_length=20,choices=LEVEL_CHOICES, default=BEGINNER)
    lessons_count = models.IntegerField(default=0)
    requirements = models.TextField()

    discount = models.PositiveIntegerField(verbose_name='Discount Percentage', default=0)
    discount_starts_at = models.DateField()
    discount_ends_at = models.DateField()

    is_active = models.BooleanField(default=True)
    has_certificate = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    def has_discount(self) -> bool:
        today = timezone.now().date()
        return self.discount_starts_at <= today <= self.discount_ends_at
    
    def duration(self):
        duration = 0
        for lesson in self.lessons.all():
            duration += lesson.duration
        return duration
    

