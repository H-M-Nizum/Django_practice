from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about),
    path('service/', views.service),
    path('contact/', views.contact),
]
