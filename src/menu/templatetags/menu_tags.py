from django import template
from menu.models import Menu, MenuItem
from menu.utils import get_all_menu_items, build_menu_tree

register = template.Library()


@register.inclusion_tag('menu/menu_template.html')
def draw_menu(menu_name):
    all_items = get_all_menu_items(menu_name)
    menu_tree = build_menu_tree(all_items)
    return {'menu_items': menu_tree.get(None), 'menu_tree': menu_tree}

