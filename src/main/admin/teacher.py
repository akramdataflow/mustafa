from main.models import Teacher
from django.contrib import admin


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'user', 'email', 'bio', 'image')
    prepopulated_fields = {'slug': ('name',)}
