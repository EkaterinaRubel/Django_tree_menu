from django.test import TestCase

from menu.models import Menu, MenuItem
from menu.utils import get_all_menu_items, build_menu_tree

class MenuUtilsTests(TestCase):
    """Test suite for menu utility functions."""

    def setUp(self):
        self.menu = Menu.objects.create(name="Test Menu")
        self.root_item = MenuItem.objects.create(name="Root Item", menu=self.menu)
        self.child_item = MenuItem.objects.create(name="Child Item", menu=self.menu, parent=self.root_item)

        self.another_menu = Menu.objects.create(name="Another Menu")
        self.another_root_item = MenuItem.objects.create(name="Another root Item", menu=self.another_menu)

    def test_get_all_menu_items(self):
        """function get_all_menu_items correctly retrieves all items for a given menu."""
        items = get_all_menu_items("Test Menu")
        self.assertIn(self.root_item, items)
        self.assertIn(self.child_item, items)

    def test_get_all_menu_items_negative(self):
        """function get_all_menu_items does not retrieve items from other menus."""
        items = get_all_menu_items("Test Menu")
        self.assertNotIn(self.another_root_item, items)

    def test_build_menu_tree(self):
        """function build_menu_tree correctly organizes menu items into a tree structure."""
        items = MenuItem.objects.filter(menu__name="Test Menu").order_by('id')
        tree = build_menu_tree(items)
        self.assertIn(self.root_item.id, tree)
        self.assertIn(self.child_item, tree[self.root_item.id])

    def test_build_menu_tree_negative(self):
        """function build_menu_tree does not include unrelated items in the tree."""
        items = MenuItem.objects.filter(menu__name="Test Menu").order_by('id')
        tree = build_menu_tree(items)
        self.assertNotIn(self.another_root_item, tree)