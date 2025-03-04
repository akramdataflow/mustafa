from django.urls import path, include
from . import views

urlpatterns = [
     path('course/', include(arg=[
          path('teachers/', views.teacher_list_view, name='teachers'),
          path('<str:slug>/', views.course_details_view, name='course_details'),
          path('', views.course_list_view, name='course_list'),
     ])),
     
     

     path('', views.home_view, name='home'),
]