from django.shortcuts import render,  get_object_or_404
from .models import *
from django.db.models import Avg

# Create your views here.
def main(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'index.html', context)


def courses(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'course.html', context)


def course_details(request,id):
    course = get_object_or_404(Course, id=id)
    courses = Course.objects.filter(title=course)
    average_rating = Review.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']
    num_enrollments = Enrollment.objects.filter(course=course).count()
    context = {'courses':courses, 'course':course, 'average_rating': average_rating, 'num_enrollments':num_enrollments, 'teacher': course.teacher}
    return render(request, 'course-details.html', context)

def teachers(request):
    courses = Course.objects.all()
    context = {'courses':courses}
    return render(request, 'teachers.html', context)