"""URL Configuration for the secondary menu of the application."""
from django.urls import path

from . import views

urlpatterns = [
    path('submenu1/', views.index, name='submenu1'),
    path('submenu2/', views.index, name='submenu1'),
]
