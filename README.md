### !!! utf-8

### su

apt install python3-venv

### pip env


pip -V

pip -h

https://pip.pypa.io/en/stable/

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment



## django010Project

### для не Windows, использовать терминал

 
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

pip list

pip freeze > requirements.txt

django-admin startproject project01 ../project01

dir

python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000

Ctrl + C

редактируем project01/settings.py

ALLOWED_HOSTS = ["*"],

python manage.py runserver 127.0.0.1:80

deactivate

#### Разворачиваем из архива 

cd project01

python3 -m venv env

. env/bin/activate

pip install --upgrade pip

pip list

pip install -r requirements.txt

python manage.py runserver

### Для Windows: 

Запускаем powershel или cmd

mkdir project01

cd project01

python -m venv .venv

.venv\Scripts\activate

Если возникли проблемы:

Вариант 1. Отрываем powershell от имени администратора и набираем и запускаем:

Set-ExecutionPolicy RemoteSigned 


Вариант 2. Открываем cmd

Продолжаем: 

python -m venv .venv

.venv\Scripts\activate

pip list

python -m pip install --upgrade pip

pip list

py -m 

pip install Django или  pip install -U django==8.0.4

Если восстанавливаем из архива) 

pip install -r requirements.txt  


pip list

django-admin startproject project01 ../project01

dir


python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000

Ctrl + C

deactivate

pip freeze > requirements.txt

### Конфигурирование и запуск после извлечения архива

python -m venv .venv

.venv\Scripts\activate

pip list

pip install -r requirements.txt

pip list

python manage.py runserver 

### При необходимости когда начнем работать с моделями
 
python manage.py mikemigrations

python manage.py migrate

python manage.py createsuperuser

admin root

### Конфигурирование и запуск Django (после GitHub)

git clone https://github.com...

cd ... 

или

mkdir ....

git init

git remote add origin ...

git pull origin main





### Редирект порта для сервера
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

### Готовим новую конфигурацию 

pip freeze > requirements.txt

