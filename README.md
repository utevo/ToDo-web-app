# ToDo-web-app
📔 This is a ToDo web app written using the Django framework.
http://35.210.152.148/todo

# Features:

- Neat & Simple Look
- User Authentication System
- Hashtags System

# Deployment:

Things you need:
- `python 3`
- `pip3`
- `pipenv or venv`

Steps:

1. Create a python virtualenv

2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Create tables:

    ```sh
    python3 manage.py migrate
    ```

4. Create a superuser:

    ```sh
    python3 manage.py createsuperuser
    ```
    
# Usage
Run the server:

    python3 manage.py runserver
    
    
# License
Licensed under [MIT](LICENSE.md) license. Copyright (c) 2019 Michał Kowieski
