"""Module provides metods for work with items."""
from menu.models import MenuItem


def get_all_menu_items(menu_name):
    """
    Retrieve all menu items associated with a given menu name.

    Args:
        menu_name (str): The name of the menu for which to retrieve items.

    Returns:
        QuerySet: A Django QuerySet containing all menu items.
    """
    return MenuItem.objects.filter(menu__name=menu_name).order_by('id')


def build_menu_tree(all_items):
    """
    Build a hierarchical tree structure from a list of menu items.

    Args:
        all_items (QuerySet): A Django QuerySet of MenuItem objects.

    Returns:
        dict: A dictionary where each key is a parent item's ID,
        and its value is a list of child items.
    """
    tree = {}
    for item in all_items:
        if item.parent_id not in tree:
            tree[item.parent_id] = []
        tree[item.parent_id].append(item)
    return tree


def get_menu_path(all_items, current_url):
    """
    Recursively build the path from the root to the active menu item.

    Args:
        all_items (QuerySet): A QuerySet of MenuItem objects to search through.
        current_url (str): current page URL to find the active menu item.

    Returns:
        list: A list of MenuItem objects
        representing the path from the root to the active item.
    """
    for item in all_items:
        if item.get_absolute_url() == current_url:
            if item.parent:
                parent_path = get_menu_path(
                    all_items,
                    item.parent.get_absolute_url(),
                )
                return parent_path + [item]
            return [item]
