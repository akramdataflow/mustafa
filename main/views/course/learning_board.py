from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.contrib.auth.decorators import login_required

from main.models import Course, Review, EnrolledCourse


@login_required
def learning_board_view(request):
    context = {'enrolled_courses':EnrolledCourse.objects.filter(user=request.user).select_related('course')}
    return render(request, 'course/learning_board.html', context)