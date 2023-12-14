"""Module contains custom template tags."""
from django import template

from menu.utils import build_menu_tree, get_all_menu_items

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu_name):
    """
    Render a hierarchical menu based on the specified menu name.

    Args:
        context (dict): The template context, includes the current request.
        menu_name (str): The name of the menu to be rendered.

    Returns:
        dict: A context dictionary containing the root menu items,
        the complete menu tree, and the current URL.
    """
    request = context['request']
    current_url = request.path
    all_items = get_all_menu_items(menu_name)
    menu_tree = build_menu_tree(all_items)
    return {
        'menu_items_no_parent': menu_tree.get(None),
        'menu_tree': menu_tree,
        'current_url': current_url,
    }
