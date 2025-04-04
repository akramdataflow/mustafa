
from django.shortcuts import render

from main.models import Course, Teacher


def teacher_list_view(request):
    context = {
        'courses': Course.objects.all().prefetch_related('teachers'),
        'teachers': Teacher.objects.all(),
    }
    return render(request, 'course/teacher/teacher_list.html', context)

def teacher_details_view(request, slug: str):
    context = {
        'courses': Course.objects.filter(teachers__slug=slug)
    }
    return render(request, 'course/teacher/teacher_details.html', context)