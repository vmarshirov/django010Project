python manage.py -h  

python manage.py startapp responseApp

смотрим ../responseApp/apps.py

'responseApp.apps.ResponseappConfig'

редактируем project01/settings.py

'responseApp.apps.ResponseappConfig',

python manage.py runserver 10.0.2.15:8000
