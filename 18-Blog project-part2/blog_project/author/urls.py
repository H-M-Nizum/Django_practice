from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('profile/', views.profileupdate, name='user_profile'),
    path('profile/pass_change/', views.password_change, name='pass_change'),
]