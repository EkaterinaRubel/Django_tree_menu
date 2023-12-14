# Django_tree_menu
Tree Menu is a Django project that implements a tree-like menu for websites. The application for creating and managing tree-like menus allows for the easy creation of multi-level menus that can be integrated into any part of your Django web site.
## Features
- **Tree-like Menu**: Supports multi-level menus with unlimited depth of nesting.
- **Management via Django Admin**: Menus and menu items can be easily created, edited, and deleted through the standard Django admin panel.
- **Template Tag**: The menu is implemented through a customizable template tag, allowing easy insertion of the menu into any template.
- **Active Menu Item**: Automatic highlighting of the active menu item based on the URL of the current page.
- **Query Optimization**: Rendering each menu requires only one query to the database.
- **Flexibility**: Supports multiple menus on a single page, identified by name.
- **URL Navigation**: Supports navigation to specified URLs, including named URLs.
- **Dynamic Menu Expansion**: Automatically collapses unnecessary menu items, showing only the items above the active item and the first level of nested items under the active item for cleaner interface.

## Technology Stack
- Django
- PostgreSQL
- unittest

## Installation
[Contributing Guidelines](CONTRIBUTING.md)