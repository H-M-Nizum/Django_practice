from django.urls import path
from . import views


urlpatterns = [
   path('about/', views.about),
   path('contact/', views.contact),
   path('context_dic/', views.context_dic),
]
