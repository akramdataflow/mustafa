from main.models import Student
from django.contrib import admin


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'masked_email', 'bio', 'image')
    search_fields = ('name', 'email')