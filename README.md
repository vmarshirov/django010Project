### django010Project


### git

git clone https://github.com...

cd ... 

или

mkdir ....

git init

git remote add origin ...

git pull origin main

## pip env


https://pip.pypa.io/en/stable/

https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment


### env - для не Windows 

su

apt install python3 -venv

exit

python3 -m venv env

. env/bin/activate

py -m pip install Django

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

deactivate

### Для Windows env: 

python -m venv env

env\Scripts\activate

py -m pip install Django

https://docs.djangoproject.com/en/4.1/intro/tutorial01/

deactivate

https://medium.com/@ph1l74/python-venv-%D0%BD%D0%B0-windows-10-2118ad685b1 

https://wiki.iphoster.net/wiki/Windows_10_-_%D0%BA%D0%B0%D0%BA_%D0%BF%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%D1%82%D1%8C_%D0%B8%D0%BB%D0%B8_%D0%B8%D0%B7%D0%BC%D0%B5%D0%BD%D0%B8%D1%82%D1%8C_%D0%BF%D0%B5%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5_%D1%81%D1%80%D0%B5%D0%B4%D1%8B_(Environment_Variable)

https://python.land/virtual-environments/virtualenv


### Установка и запуск



### Конфигурирование и запуск Django (после GitHub)

pip install -r requirements.txt

python manage.py runserver 10.0.2.15:8000


python manage.py migrate

python manage.py createsuperuser

admin rootgit 


------------

### Редирект порта для сервера
iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 80 -j REDIRECT --to-port 8000

-------------=

pip freeze > requirements.txt


--------------------


