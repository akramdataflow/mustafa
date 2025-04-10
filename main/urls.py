from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
     path('api/', include(arg=[
         path('payment/webhook/', views.PaymentWebhookAPIView.as_view(), name='payment_webhook_api'),
     ])),
     path('about/', views.about_view, name='about'),
     path('contact/', views.contact_view, name='contact'),
     path('login/', views.user_login, name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
     path('signup/', views.signup_view, name='signup'),
     path('course/', include(arg=[
          path('teachers/', views.teacher_list_view, name='teachers'),
          path('teachers/<str:slug>/', views.teacher_details_view, name='teacher_details'),
          path('learning-board/', views.learning_board_view, name='learning_board'),
          path('<str:course_slug>/<str:lesson_slug>/preview/', views.lesson_preview_view, name='lesson_preview'),
          path('<str:slug>/', views.course_details_view, name='course_details'),
          path('', views.course_list_view, name='course_list'),
     ])),
     path('cart/', include(arg=[
        path('to/add/<str:course_slug>/', views.add_to_cart_view, name='add_to_cart'),
        path('from/remove/<str:course_slug>/', views.remove_from_cart_view, name='remove_from_cart'),
        path('join/<str:course_slug>/', views.join_course_view, name='join_course'),
     ])),
     #path('order/', include(arg=[
     #    path('details/<int:id_>/', views.order_details, name='order_details'),
     #    path('history/', views.order_history, name='order_history'),
     #])),
     path('payment/', views.payment_page, name='payment_page'),  # Payment page
     path('payment-status/', views.payment_status, name='payment_status'),  # Success page
     path('', views.home_view, name='home'),
]