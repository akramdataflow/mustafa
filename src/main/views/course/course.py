from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

from main.models import Course, Review, EnrolledCourse


def course_list_view(request):
    context = {'courses':Course.objects.all()}
    return render(request, 'course/course_list.html', context)


def course_details_view(request, slug: str):
    course = get_object_or_404(Course, slug=slug)
    average_rating = Review.objects.filter(course=course).aggregate(Avg('rating'))['rating__avg']
    num_enrollments = EnrolledCourse.objects.filter(course=course).count()
    context = {
        'courses': Course.objects.filter(name=course.name), 
        'course': course, 
        'average_rating': average_rating, 
        'num_enrollments':num_enrollments, 
        'teachers': course.teachers
    }
    return render(request, 'course/course_details.html', context)
