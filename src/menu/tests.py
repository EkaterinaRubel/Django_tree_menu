from django.test import TestCase
from django.urls import reverse

from menu.models import Menu, MenuItem
from menu.utils import build_menu_tree, get_all_menu_items

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


class MenuItemModelTests(TestCase):
    """Test suite for reverse url by named url."""

    def setUp(self):
        self.menu = Menu.objects.create(name="Test Menu")
        self.item_with_named_url = MenuItem.objects.create(
            name="Named URL Item",
            menu=self.menu,
            url_name="home"
        )
        self.item_with_explicit_url = MenuItem.objects.create(
            name="Explicit URL Item",
            menu=self.menu,
            url="/explicit-url/"
        )

    def test_get_absolute_url_with_named_url(self):
        """get_absolute_url returns the correct URL for an item with a named URL.""" 
        expected_url = reverse("home")
        self.assertEqual(self.item_with_named_url.get_absolute_url(), expected_url)

    def test_get_absolute_url_with_explicit_url(self):
        """get_absolute_url returns the explicitly defined URL for an item."""
        self.assertEqual(self.item_with_explicit_url.get_absolute_url(), "/explicit-url/")
