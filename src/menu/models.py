from django.db import models
from django.urls import reverse

class Menu(models.Model):
    """
    Model representing a menu.

    Each menu can contain multiple menu items.
    """

    name = models.CharField(
        max_length=50, unique=True, verbose_name='Menu Name',
    )
    description = models.TextField(
        max_length=300, blank=True, verbose_name='Description',
    )

    class Meta:
        """Configuration class."""

        ordering = ['id']
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """
    Model representing an item in a menu.

    Each menu item is linked to a parent menu
    and can have a hierarchical structure.
    """

    name = models.CharField(
        max_length=50, unique=True, verbose_name='Menu Item Name',
    )
    description = models.TextField(
        max_length=300, blank=True, verbose_name='Description',
    )
    url = models.CharField(
        max_length=200, blank=True, verbose_name='External URL',
        help_text='Specify for redirecting to an external resource '
        'from this menu item. If not specified, the system will try '
        'to find child items to create a submenu.',
    )
    url_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Named URL',
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True,
        verbose_name='Parent Item',
        )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='menu_items',
        verbose_name='Menu',
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Menu Item'
        verbose_name_plural = 'Menu Items'

    def get_absolute_url(self):
        if self.url_name:
            return reverse(self.url_name)
        return self.url
    
    def __str__(self):
        return self.name
