from main.models import EnrolledCourse
from django.contrib import admin


@admin.register(EnrolledCourse)
class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')