from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('', include('menu.urls_main_menu')),
    path('', include('menu.urls_secondary_menu')),
]