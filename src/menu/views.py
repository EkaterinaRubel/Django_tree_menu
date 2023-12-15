"""This module contains view functions for the 'menu' application."""
from django.shortcuts import render


def index(request):
    return render(request, 'menu/base.html')
