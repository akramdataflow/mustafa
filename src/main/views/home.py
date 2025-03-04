from django.shortcuts import render

from main.models import Course
from django.contrib.auth.models import User


def home_view(request):
    courses = Course.objects.all()
    users = User.objects.all()
    users_count = users.count()
    courses_count = courses.count()
    context = {'courses':courses, 'users':users, 'users_count':users_count, 'courses_count':courses_count}
    return render(request, 'home.html', context)