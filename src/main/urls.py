from django.urls import path, include
from . import views

urlpatterns = [
     path('about/', views.about_view, name='about'),
     path('contact/', views.contact_view, name='contact'),
     path('course/', include(arg=[
          path('teachers/', views.teacher_list_view, name='teachers'),
          path('teachers/<str:slug>/', views.teacher_details_view, name='teacher_details'),
          path('<str:slug>/', views.course_details_view, name='course_details'),
          path('', views.course_list_view, name='course_list'),
     ])),
      path('', views.home_view, name='home'),
]