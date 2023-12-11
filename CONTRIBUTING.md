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
#### Preparing DataBase
Run the Docker container with the database.
```
docker compose up postgres
```
Create the database by executing the file `tools/db_initialization.sql`.
Create the tables for INSTALLED_APPS.
```
cd src
python manage.py migrate
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
#### Start development server
```
cd src 
python3 manage.py runserver
```

### Testing
```
python manage.py test menu
```