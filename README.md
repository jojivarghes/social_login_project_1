# social_login_project_1

A demo social login project with Django 

## Setup

1. Install requirements.txt

        pip install -r requirements.txt
    
 
1. Create Postgres DB named "social_login_db"

        CREATE DATABASE social_login_db_1;

1. Rename file ".env_template" to ".env" and update settings in it before execution
1. Run the Django project

        python manage.py makemigrations
        python manage.py migrate
        python manage.py createsuperuser
        python manage.py runserver
        
1. Check http://127.0.0.1:8000/
