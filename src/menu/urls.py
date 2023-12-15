"""This module defines URL patterns for the 'menu' application."""
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('menu.urls_main_menu')),
    path('', include('menu.urls_secondary_menu')),
]
