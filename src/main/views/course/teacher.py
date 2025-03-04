
from django.shortcuts import render

from main.models import Course


def teacher_list_view(request):
    context = {
        'courses': Course.objects.all().prefetch_related('teachers')
    }
    return render(request, 'course/teacher/teacher_list.html', context)
