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





![1](https://github.com/user-attachments/assets/44a1a7ff-8f02-461b-a42a-46dac42f961f)




![2](https://github.com/user-attachments/assets/412b320f-87a2-48da-8a8c-e578eda05065)





![3](https://github.com/user-attachments/assets/615e5217-ed34-4676-9e55-dc3c9f2837f1)






![4](https://github.com/user-attachments/assets/d2baa267-0664-451b-9799-d3902c47ca8d)






![5](https://github.com/user-attachments/assets/c6aac6b5-f226-46cb-b9e6-724f4dbee734)









































