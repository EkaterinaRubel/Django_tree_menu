#!/bin/bash
set -e

# Waiting for PostgreSQL to start
until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DATABASE_HOST" -U "$POSTGRES_USER" -c '\q'; do
  >&2 echo "PostgreSQL is unavailable - sleeping"
  sleep 1
done

>&2 echo "PostgreSQL is up - executing command"

# Creating the database if it doesn't exist
PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DATABASE_HOST" -U "$POSTGRES_USER" -tc "SELECT 1 FROM pg_database WHERE datname = 'django_tree_menu'" | grep -q 1 || PGPASSWORD=$POSTGRES_PASSWORD psql -h "$DATABASE_HOST" -U "$POSTGRES_USER" -c "CREATE DATABASE django_tree_menu"

# Changing to the Django application's working directory
cd /django_tree_menu/src

# Applying migrations
python manage.py migrate

# Creating a superuser
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" | python manage.py shell

# Returning to the original directory
cd -

# Starting the main process (e.g., Django server)
exec "$@"
