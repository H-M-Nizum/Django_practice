from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('signup/', views.Signup, name='signup'),
   path('login/', views.userlogin, name='login'),
   path('logout/', views.userlogout, name='logout'),
   path('profile/', views.profile, name='profile'),
]
