"""Module contains custom template filters."""
from django import template

register = template.Library()


@register.filter
def get(dictionary, key):
    """
    Get a value from a dictionary using a key.

    Args:
        dictionary (dict): dictionary.
        key: The key for which to retrieve the value.

    Returns:
        The value associated with the specified key in the dictionary.
    """
    return dictionary.get(key)
