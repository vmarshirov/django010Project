### !!! utf-8

### su

apt install python3-venv

### pip env


pip -V

pip -h

https://pip.pypa.io/en/stable/

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment


### Для Windows: 

Запускаем powershel (поиск - powershel) или cmd (поиск - командная строка или windows+R  затем cmd)

mkdir fio_project

cd fio_project


python -m venv .venv

ls

.venv\Scripts\activate

Если возникли проблемы:

Вариант 1. Отрываем powershell от имени администратора и набираем и запускаем:

Set-ExecutionPolicy RemoteSigned 


Вариант 2. Открываем cmd (windows+R)

Продолжаем: 


.venv\Scripts\activate

pip list

deactivate

python -m pip install --upgrade pip

pip list

py -m 

pip install Django 

или  

pip install -U django==8.0.4


django-admin startproject fio_project ./

pip freeze > requirements.txt

pip install -r requirements.txt 

python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000

Ctrl + C

deactivate


### Если восстанавливаем из архива) 

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt  

python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000


### для не Windows, использовать терминал

apt-get update

apt install python3 -venv

### для MacOs, использовать терминал

mkdir fio_project

cd fio_project

ls -laF

python3 -m venv .venv

. .venv/bin/activate или source venv/bin/activate 

pip list

pip install Django или  pip install -U django==8.0.4 


django-admin startproject fio_project ./

pip freeze > requirements.txt

pip install -r requirements.txt 

python manage.py runserver или (если уникальный ip)  python manage.py runserver 10.0.2.15:8000

Ctrl + C

deactivate

Ctrl + C

#### Разворачиваем из архива 

python3 -m venv .venv

. .venv/bin/activate

pip list

pip install -r requirements.txt

python manage.py runserver


## Полезно для всех

редактируем /settings.py

ALLOWED_HOSTS = ["*"],



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

sudo iptables -A PREROUTING -t nat -p tcp --dport 80 -j REDIRECT --to-ports 8080

