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

python -m pip install Django

pip install -U django==8.0.4

cd ../

django-admin startproject project01 project01

cd project01

vim project01/settings.py

ALLOWED_HOSTS = ["*"]

python manage.py runserver 10.0.2.15:8000

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

deactivate

### Для Windows: 

python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip 

py -m pip install Django

django-admin startproject ProjectName ../ProjectName

ALLOWED_HOSTS = ["*"]

python manage.py runserver 10.0.2.15:8000


https://docs.djangoproject.com/en/4.1/intro/tutorial01/

deactivate

https://medium.com/@ph1l74/python-venv-%D0%BD%D0%B0-windows-10-2118ad685b1 

https://wiki.iphoster.net/wiki/Windows_10_-_%D0%BA%D0%B0%D0%BA_%D0%BF%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C_%D0%B8%D0%BB%D0%B8_%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C_%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%80%D0%B5%D0%B4%D1%8B_(Environment_Variable)

https://python.land/virtual-environments/virtualenv


## AppName

python manage.py -h

python manage.py startapp AppName


### Конфигурирование и запуск Django (после GitHub)

git clone https://github.com...

cd ... 

или

mkdir ....

git init

git remote add origin ...

git pull origin main


### Окончательное конфигурирование и запуск

cd django010Project

python3 -m venv env

. env/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

vim django010Project/settings.py

python manage.py runserver 185.46.9.94:8000

python manage.py migrate

python manage.py createsuperuser

admin root


### Редирект порта для сервера
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

### Готовим новую конфигурацию 

pip freeze > requirements.txt

