from django.contrib import admin
from .models import *

admin.site.register(Course)
admin.site.register(CourseContent)
admin.site.register(Enrollment)
admin.site.register(Review)