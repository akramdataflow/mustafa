from main.models import Course
from django.contrib import admin


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):    
    list_display = ('name', 'category', 'price')