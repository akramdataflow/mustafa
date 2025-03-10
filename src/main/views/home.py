from django.shortcuts import render

from main.models import Course, Teacher, Student
from django.contrib.auth.models import User


def home_view(request):
    courses = Course.objects.all()
    teachers = Teacher.objects.all()
    context = {
        'courses':courses, 
        'teachers': teachers,
        'teacher_count': teachers.count(), 
        'student_count': Student.objects.count(), 
        'course_count':courses.count(),
    }
    return render(request, 'home.html', context)

