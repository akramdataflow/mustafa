from main.models import EnrolledCourse
from django.contrib import admin


@admin.register(EnrolledCourse)
class EnrolledCourseAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'price', 'currency', 'is_active', 'is_completed')
    list_filter = ('is_active', 'is_completed')
    search_fields = ('user__username', 'course__name')
    date_hierarchy = 'created'
