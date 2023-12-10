from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/', views.Signup, name='signup'),
   path('login/', views.userlogin, name='login'),
   path('logout/', views.userlogout, name='logout'),
   path('pass_change/', views.passward_change, name='passwordChange'),
   path('pass_change2/', views.passward_change2, name='passwordChange2'),
   path('profile/', views.profile, name='profile'),
]
