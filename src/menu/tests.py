"""This module contains unit tests for the 'menu' application."""
from django.test import TestCase
from django.urls import reverse

from menu.models import Menu, MenuItem
from menu.utils import build_menu_tree, get_all_menu_items, get_menu_path


class GetAllMenuItemsTests(TestCase):
    """Test suite for get_all_menu_items function."""

    def setUp(self):
        """Set up test data for get_all_menu_items tests."""
        self.menu = Menu.objects.create(name='Test Menu')
        self.root_item = MenuItem.objects.create(
            name='Root Item',
            menu=self.menu,
        )
        self.child_item = MenuItem.objects.create(
            name='Child Item',
            menu=self.menu,
            parent=self.root_item,
        )

        self.another_menu = Menu.objects.create(name='Another Menu')
        self.another_root_item = MenuItem.objects.create(
            name='Another root Item',
            menu=self.another_menu,
        )

    def test_get_all_menu_items(self):
        """The get_all_menu_items retrieves all items for a given menu."""
        items = get_all_menu_items('Test Menu')
        self.assertIn(self.root_item, items)
        self.assertIn(self.child_item, items)

    def test_get_all_menu_items_negative(self):
        """The get_all_menu_items does not retrieve items from other menus."""
        items = get_all_menu_items('Test Menu')
        self.assertNotIn(self.another_root_item, items)


class BuildMenuTreeTests(TestCase):
    """Test suite for build_menu_tree function."""

    def setUp(self):
        """Set up test data for build_menu_tree tests."""
        self.menu = Menu.objects.create(name='Test Menu')
        self.root_item = MenuItem.objects.create(
            name='Root Item',
            menu=self.menu,
        )
        self.child_item = MenuItem.objects.create(
            name='Child Item',
            menu=self.menu,
            parent=self.root_item,
        )

        self.another_menu = Menu.objects.create(name='Another Menu')
        self.another_root_item = MenuItem.objects.create(
            name='Another root Item',
            menu=self.another_menu,
        )

    def test_build_menu_tree(self):
        """The build_menu_tree correctly organizes a tree structure."""
        items = MenuItem.objects.filter(menu__name='Test Menu').order_by('id')
        tree = build_menu_tree(items)
        self.assertIn(self.root_item.id, tree)
        self.assertIn(self.child_item, tree[self.root_item.id])

    def test_build_menu_tree_negative(self):
        """The build_menu_tree does not include unrelated items in the tree."""
        items = MenuItem.objects.filter(menu__name='Test Menu').order_by('id')
        tree = build_menu_tree(items)
        self.assertNotIn(self.another_root_item, tree)


class MenuItemModelTests(TestCase):
    """Test suite for reverse url by named url."""

    def setUp(self):
        """Set up test data for the menu item tests."""
        self.menu = Menu.objects.create(name='Test Menu')
        self.item_with_named_url = MenuItem.objects.create(
            name='Named URL Item',
            menu=self.menu,
            url_name='home',
        )
        self.item_with_explicit_url = MenuItem.objects.create(
            name='Explicit URL Item',
            menu=self.menu,
            url='/explicit-url/',
        )

    def test_get_absolute_url_with_named_url(self):
        """get_absolute_url returns the correct URL by named URL."""
        expected_url = reverse('home')
        self.assertEqual(
            self.item_with_named_url.get_absolute_url(),
            expected_url,
        )

    def test_get_absolute_url_with_explicit_url(self):
        """get_absolute_url returns the explicitly defined URL for an item."""
        self.assertEqual(
            self.item_with_explicit_url.get_absolute_url(),
            '/explicit-url/',
        )


class MenuPathTests(TestCase):
    """Test suite for get_menu_path functions."""

    def setUp(self):
        """Set up test data for the menu path tests."""
        self.test_menu = Menu.objects.create(name='Test Menu')
        self.root_item = MenuItem.objects.create(
            name='Root',
            url='/root',
            menu=self.test_menu,
        )
        self.child_item = MenuItem.objects.create(
            name='Child',
            url='/child',
            parent=self.root_item,
            menu=self.test_menu,
        )

    def test_path_to_root_item(self):
        """The path to a root menu item is correctly identified."""
        all_items = MenuItem.objects.all()
        path = get_menu_path(all_items, '/root')
        self.assertEqual(path, [self.root_item])

    def test_path_to_child_item(self):
        """The path to a child menu item is correctly identified."""
        all_items = MenuItem.objects.all()
        path = get_menu_path(all_items, '/child')
        self.assertEqual(path, [self.root_item, self.child_item])

    def test_path_with_invalid_url(self):
        """Test the function with an invalid URL."""
        all_items = MenuItem.objects.all()
        path = get_menu_path(all_items, '/invalid-url')
        self.assertEqual(path, None)

    def test_empty_menu_items(self):
        """Test the function with an empty QuerySet."""
        path = get_menu_path(MenuItem.objects.none(), '/root')
        self.assertEqual(path, None)
