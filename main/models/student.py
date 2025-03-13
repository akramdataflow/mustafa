import uuid

from django.db import models
from django.conf import settings

from autoslug import AutoSlugField


def file_upload(instance, filename):
    file_name, extension = filename.split('.')
    return f"students/{uuid.uuid4().hex}_{file_name}.{extension}"


class Student(models.Model):
    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    email = models.EmailField(max_length=254)
    bio = models.TextField()
    image = models.ImageField(upload_to=file_upload)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
    
    def enrolled_courses(self):
        from .enrollment import EnrolledCourse
        return EnrolledCourse.objects.filter(user=self.user)
    
    def masked_email(self):
        return f"{self.email[:2]}...{self.email[-2:]}"
    
    def masked_phone_number(self):
        return f"{self.phone_number[:2]}...{self.phone_number[-2:]}"
