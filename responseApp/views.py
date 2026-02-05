import datetime

from django.http import HttpResponse

# https://docs.djangoproject.com/en/4.1/topics/http/urls/
# https://docs.djangoproject.com/en/4.1/topics/http/views/


def index(request):
    # http://127.0.0.1:8000/responseApp/
    return HttpResponse("responseApp")


def html(request):
    # http://127.0.0.1:8000/responseApp/html/
    now = datetime.datetime.now()
    # html = "<html><body>Сейчас %s.</body></html>" % now
    # return HttpResponse(html)
    return HttpResponse(f"<html><body>It is now {now}.</body></html>")


def calculate_get(request):
    # Получаем параметры x и y из строки запроса (GET)
    # http://127.0.0.1:8000/responseApp/calculate?x=1&y=2
    print(request)
    x_str = request.GET.get("x", "0")
    y_str = request.GET.get("y", "0")

    try:
        x = float(x_str)
        y = float(y_str)
        z = x + y
        result = f"<h1>Калькулятор GET</h1><p>x = {x}</p><p>y = {y}</p><h2>z = x + y = {z}</h2>"
    except ValueError:
        result = "<h1>Ошибка</h1><p>Пожалуйста, передайте числовые значения для x и y в строке запроса. Пример: <code>?x=10&y=5</code></p>"
    return HttpResponse(result)


def f_str(request, str_value):
    # http://127.0.0.1:8000/responseApp/f_str/abc
    print("str_value: ", str_value)

    return HttpResponse(f"<p>f_str, str_value:  {str_value}</p>")


def f_int(request, int_value):
    # http://127.0.0.1:8000/responseApp/f_int/12345
    print(type(int_value), int_value)
    return HttpResponse(f"f_int, int_value: {int_value} ")


def f_slug(request, slug_value):
    # http://127.0.0.1:8000/responseApp/f_slug/building-your_1st-django-site
    print(type(slug_value), slug_value)
    return HttpResponse(f"f_slug, slug_value: {slug_value}")


def f_str_int_slug(request, str_value, int_value, slug_value):
    # http://127.0.0.1:8000/responseApp/f_str_int_slug/x=1&y=2/123/1st-django-site
    print(type(str_value), str_value)
    print(type(int_value), int_value)
    print(type(slug_value), slug_value)
    return HttpResponse(
        f"f_str,  str_value: {str_value} <br>f_int, f_int: {int_value} <br>f_slug, slug_value: {slug_value}"
    )


def f_path(request, path_value):
    # http://127.0.0.1:8000/responseApp/f_path/building/your-1st/x=1
    print("path_value: ", path_value)
    path_elements = path_value.split("/")
    print("path_elements:", path_elements)
    x = (path_elements[2].split("="))[1]
    print("x: ", x)
    # path_elements_amount = path_elements.__len__()
    # print("path_elements_amount", path_elements_amount)
    # print(dir(request))
    # print("request.path: ", request.path)
    # request_path_elements = request.path.split("/")
    # print("request_path_elements:", request_path_elements)
    # request_elements_amount = request_path_elements.__len__()
    # print(request_elements_amount)
    # last_request_path_element = request_path_elements[request_elements_amount  - 1 ]
    # print(last_request_path_element)
    return HttpResponse(f"x:  {x}")


# Заметки на будущее
# Передать несколько переменых и произвести вычисления
# Передать несколько символов,  сформировать словарь и произвести манипуляции со словарем используя возможности Python

# signs = {'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).', 'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).', 'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).', 'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).', 'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).', 'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).', 'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).', 'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).', 'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).', 'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).', 'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).', 'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).'}
# -по названию знака (sign) вывести его описание
# -по порядковому номеру месяца вывести знак и описание
# signs[sign_of_zodiac.lower()], l = list(signs.values())
# if sign in signs:
# else:


# Arias of square, circle, rectangle
# math.pi ()
