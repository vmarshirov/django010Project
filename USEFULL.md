# to rename a django project

Rename the oldprojectname directory to newprojectname

manage.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldprojectname.settings')

newprojectname/wsgi.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldprojectname.settings')

newprojectname/settings.py: Change ROOT_URLCONF = 'oldprojectname.urls' and change WSGI_APPLICATION = 'oldprojectname.wsgi.application'

newprojectname/urls.py: Change oldprojectname in a line I had added

https://pyquestions.com/easy-way-to-rename-a-django-project
