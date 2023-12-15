#####  Instructions for macOS Operating System
### Setting Up the Working Environment
- Add the root directory to `PYTHONPATH` (temporarily): 
    ```
    export PYTHONPATH="$PYTHONPATH:."
    ```
- Install and activate Poetry.
    ```
    poetry install
    poetry shell
    ```

### Starting development server 
### in Docker
Build image 
```
docker build -t tree_menu:1 .
```
Start
```
docker compose up
```
### Locally
#### Preparing DataBase
Run the Docker container with the database.
```
docker compose up postgres
```
Create the database
```
docker exec -it postgres_conteiner bash
psql -U admin
CREATE DATABASE django_tree_menu;
exit
exit
```
Migrations was created by command:
```
python manage.py makemigrations menu
```
Run migrate.
```
python manage.py migrate
```
#### Preparing superuser
Create a user who can login to the admin site.
```
python manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: password
```
#### Start development server locally
```
python3 src/manage.py runserver
```

### Testing
```
python src/manage.py test menu
```
### Instructions for Populating the Database for UI/UX Testing
If you wish to visually test and interact with the menu system, you have a couple of options to populate the database with test data:
1. **Using SQL Script**: You can use the provided SQL script `tools/db_schema/db_insert_test_data.sql` to quickly populate the database with predefined data. 
2. **Using the Admin Panel**: Alternatively, you can manually enter data through the Django admin panel.