"""URL Configuration for the main menu of the application."""
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.index, name='about'),
    path('contact/', views.index, name='contact'),
    path('home/sub1/', views.index, name='home_sub1'),
    path('home/sub2/', views.index, name='home_sub2'),
    path('home/sub1/sub1/', views.index, name='home_sub1_sub1'),
    path('home/sub1/sub2/', views.index, name='home_sub1_sub2'),
    path('home/sub1/sub1/sub1/', views.index, name='home_sub1_sub1_sub1'),
]
