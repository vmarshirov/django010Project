python manage.py -h  

python manage.py startapp responseApp

смотрим ../responseApp/apps.py

'responseApp.apps.ResponseappConfig'

редактируем project01/settings.py

'responseApp.apps.ResponseappConfig',

python manage.py runserver

http://127.0.0.1:8000/responseApp
