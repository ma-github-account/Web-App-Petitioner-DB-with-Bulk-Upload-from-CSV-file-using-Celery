This application is a petitioner database. Main view contains general information about the application. Petitioner list view contains a list of all database records with links to detail views. It also contains the link to bulk upload view, where user can upload new records from csv file. Upload is fast because it is handled by celery worker using redis database.

Prerequisites:

- pip install django==5.0.7
- pip install celery==5.4.0
- pip install python-decouple==3.8
- pip install django-crispy-forms==2.3
- pip install crispy-bootstrap5==2024.2
- pip install django-ckeditor==6.7.1
- pip install beautifulsoup4==4.12.3
- pip install redis==5.0.7

How to run:

1.In first command line terminal we initialize redis database:
redis-server

2.In second command line we initialize celery worker. Command needs to be run in folder petitioner_database, where subfolder main is present.
The command:
celery -A main worker --pool=solo

3.In third command line terminal we initialize django project:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
