from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name = 'index'),
    path('loginpage.html', views.loginpage, name='loginpage'),
    path('signup.html', views.signup, name = 'signup'),
    path('user-dashboard.html', views.user_dashboard, name='user-dashboard'),
    path('index.html', views.index),
    path('success/', views.success, name = 'success'),
    path('letter_create', views.letter_create, name='letter_create'),
    path('update_letter/<int:letter_id>/', views.update_letter, name='update_letter'),
    path('delete-letter/<int:letter_id>/', views.delete_letter, name='delete-letter'),
    path('get_letter/<int:letter_id>/', views.get_letter, name='get_letter'),
]


# JESS STRUCTURE.


# urlpatterns = [
#     path('', views.letter_list, name='letter_list'),
#     path('create/', views.letter_create, name='letter_create'),
#     path('update/<int:pk>/', views.letter_update, name='letter_update'),
#     path('delete/<int:pk>/', views.letter_delete, name='letter_delete'),
# ]
