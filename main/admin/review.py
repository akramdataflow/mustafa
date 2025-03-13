from main.models import Review
from django.contrib import admin

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'rating', 'body')
    list_filter = ('rating',)