## Django tree menu changelog

### 0.1.0

#### task-1: Added poetry and basic documentations
Added the Poetry dependency manager and essential documentation and tools including README.md, CONTRIBUTING.md, CHANGELOG.md, .gitignore, .flake8

#### task-2: Created Django app
Created `tree_menu` project and `menu` app. 

#### task-3: Replaced SQLite with PostgreSQL
Added connection to database PostgreSQL.

#### task-4: Created models and migrations
Created models Menu, MenuItem and ran migrations.

#### task-5: Implemented menu editing in the admin panel
Implemented menu editing in the standard Django admin panel.

#### task-6: Added basic tree menu
Added basic tree menu.

#### task-7: Added django-debug-toolbar
Added django-debug-toolbar for inspection SQL queries.

#### task-8: Implemented URL handling in menu items
Enhanced menu items to support both explicit and named URLs for navigation.

#### task-9: Implemented active menu item determining based on current URL
The active menu item is identified and styled using CSS.

#### task-10: Implemented menu expansion to the active item and its hierarchy
All menu items above the active item and the first level of items below it are expanded.

#### task-11: Performed code refactoring 
Improved code styling to PEP 8 standards, adding docstrings.

#### task-12: Dockerized django app and added initialization script
Wrapped the Django application in a Docker container. Created an initialization script (`init-script.sh`) to creation database, migrations, and superuser.