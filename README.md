### !!! utf-8

### su

apt install python3-venv

### pip env


pip -V

pip -h

https://pip.pypa.io/en/stable/

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment



## django010Project

### для не Windows
### env  
 
su

apt-get update

apt install python3 -venv

exit

cd

mkdir project01

cd project01

python3 -m venv env

. env/bin/activate

pip install --upgrade pip

pip list

py -m pip install Django или  pip install -U django==8.0.4 или (если восстанавливаем из архива) pip install -r requirements.txt  

pip freeze > requirements.txt

django-admin startproject project01 ../project01

python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000

python manage.py -h  

python manage.py startapp responseApp

cat ../responseApp/apps.py

'responseApp.apps.ResponseAppConfig'

vim project01/settings.py

'responseApp.apps.ResponseAppConfig',

ALLOWED_HOSTS = ["*"],

python manage.py runserver 10.0.2.15:8000

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

deactivate

### Для Windows: 

Запускаем powershel или cmd

mkdir project01

cd project01

python -m venv env

env\Scripts\activate

Если возникли проблемы:

Вариант 1. Отрываем powershell от имени администратора и исполняем: Set-ExecutionPolicy RemoteSigned 

Полезно изучить: https://medium.com/@ph1l74/python-venv-%D0%BD%D0%B0-windows-10-2118ad685b1  и https://python.land/virtual-environments/virtualenv

Вариант 2. Открываем cmd

Продолжаем: 

python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip

pip list

py -m pip install Django или  pip install -U django==8.0.4 или (если восстанавливаем из архива) pip install -r requirements.txt  

pip freeze > requirements.txt

django-admin startproject project01 ../project01

python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000

python manage.py -h  

python manage.py startapp responseApp

cat ../responseApp/apps.py

'responseApp.apps.ResponseAppConfig'

vim project01/settings.py

'responseApp.apps.ResponseAppConfig',

ALLOWED_HOSTS = ["*"],

python manage.py runserver 10.0.2.15:8000

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

deactivate




### Конфигурирование и запуск Django (после GitHub)

git clone https://github.com...

cd ... 

или

mkdir ....

git init

git remote add origin ...

git pull origin main


### Окончательное конфигурирование и запуск


pip install -r requirements.txt

vim django010Project/settings.py

python manage.py runserver 185.46.9.94:8000

python manage.py mikemigrations

python manage.py migrate

python manage.py createsuperuser

admin root


### Редирект порта для сервера
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

### Готовим новую конфигурацию 

pip freeze > requirements.txt

