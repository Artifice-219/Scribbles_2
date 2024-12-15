from django.urls import path
from . import views

urlpatterns = [

    path('loginpage.html', views.loginpage),
    path('signup.html', views.signup, name = 'signup'),
    path('user-dashboard.html', views.user_dashboard),
    path('index.html', views.index),
    path('success/', views.success, name = 'success'),
    path('', views.letter_list, name='letter_list'),
    path('create/', views.letter_create, name='letter_create'),
    path('update/<int:pk>/', views.letter_update, name='letter_update'),
    path('delete/<int:pk>/', views.letter_delete, name='letter_delete'),
]


# JESS STRUCTURE.


# urlpatterns = [
#     path('', views.letter_list, name='letter_list'),
#     path('create/', views.letter_create, name='letter_create'),
#     path('update/<int:pk>/', views.letter_update, name='letter_update'),
#     path('delete/<int:pk>/', views.letter_delete, name='letter_delete'),
# ]
