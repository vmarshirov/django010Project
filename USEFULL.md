
# to rename a django project

Rename the oldprojectname directory to newprojectname

manage.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldprojectname.settings')

newprojectname/wsgi.py: Change os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oldprojectname.settings')

newprojectname/settings.py: Change 

ROOT_URLCONF = 'oldprojectname.urls' and change 

WSGI_APPLICATION = 'oldprojectname.wsgi.application'

newprojectname/urls.py: Change oldprojectname in a line I had added

https://pyquestions.com/easy-way-to-rename-a-django-project


# изменить имя приложения в Django

Переименуйте папку, которая находится в корневом каталоге проекта

Измените любые ссылки на ваше приложение в своих зависимостях, то есть файлы приложений views.py, urls.py, 'manage.py' и settings.py.

Измените таблицу базы данных django_content_type следующей командой: UPDATE django_content_type SET app_label='<NewAppName>' WHERE app_label='<OldAppName>'

  https://overcoder.net/q/902/%D0%BA%D0%B0%D0%BA-%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C-%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-django
  
  https://odwyer.software/blog/how-to-rename-an-existing-django-application#:~:text=How%20to%20rename%20an%20existing%20Django%20application%201,...%205%20Step%205%20Deploy%20your%20project%21%20

