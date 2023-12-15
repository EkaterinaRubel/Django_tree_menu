"""Module for registering models with the Django admin interface."""
from django.contrib import admin

from .models import Menu, MenuItem

admin.site.register(Menu)
admin.site.register(MenuItem)
