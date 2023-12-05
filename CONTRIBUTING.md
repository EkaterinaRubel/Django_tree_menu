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
```
cd src 
python manage.py runserver
```