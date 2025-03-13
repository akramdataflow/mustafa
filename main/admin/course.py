from main.models import Course, Lesson
from django.contrib import admin


class LessonInlineAdmin(admin.TabularInline):
    model = Lesson
    extra = 0


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInlineAdmin
               ]
    list_display = ('name', 'category', 'price', 'currency', 'discount', 'discount_starts_at', 'discount_ends_at', 'is_active', 'has_certificate',)
    search_fields = ('name', 'category', 'price', 'currency', 'discount',)
    date_hierarchy = 'created'
