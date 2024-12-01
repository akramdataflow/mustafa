from django.urls import path
from . import views

urlpatterns = [
     path('', views.main, name='home'),
     path('courses/', views.courses, name='courses'),
     path('courses/<int:id>/', views.course_details, name='course_details'),
     path('teachers/', views.teachers, name='teachers'),
]