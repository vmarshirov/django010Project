from django.http import HttpResponse
import datetime

# https://docs.djangoproject.com/en/4.1/topics/http/urls/
# https://docs.djangoproject.com/en/4.1/topics/http/views/


def index(request):  # http://127.0.0.1:8000/helloApp/
    return HttpResponse("helloApp")


def html(request):  # http://127.0.0.1:8000/helloApp/html/
    now = datetime.datetime.now()
    html = "<html><body>Сейчас %s.</body></html>" % now
    return HttpResponse(html)
    # return HttpResponse(f"<html><body>It is now {now}.</body></html>")


def f_str(request, str_value):  # http://127.0.0.1:8000/helloApp/f_str/abc
    print("type(request), request: ", type(request), request.path)
    print("request.META:", request.META.get("HTTP_HOST"))
    path_elements = request.path.split("/")
    elements_amount = path_elements.__len__()
    path_element = path_elements[elements_amount - 2]
    print("type(str_value), str_value: ", type(str_value), str_value)
    return HttpResponse(
        f"<p>f_str, str_value.capitalize():  {str_value.capitalize()}; \n<br>path_element: {path_element} \n</p>")


def f_int(request, int_value):  # http://127.0.0.1:8000/helloApp/f_int/12345
    print(type(int_value), int_value)
    return HttpResponse(f"f_int, int_value: {int_value} ")


def f_slug(request, slug_value):# http://127.0.0.1:8000/helloApp/f_slug/building-your/1st-django-site
    print(type(slug_value), slug_value)
    return HttpResponse(f"f_slug, slug_value: {slug_value}")


def f_path(request, path_value): # http://127.0.0.1:8000/helloApp/f_path/building/your-1st/django-site
    print("request: ", request.path)
    print("type(request): ", type(request))
    print("request.META:", request.META.get("HTTP_HOST"))
    path_elements = request.path.split("/")
    print('path_elements:', path_elements)
    elements_amount = path_elements.__len__()
    path_element = path_elements[elements_amount - 1]
    return HttpResponse(f"path_element: {path_element}")

# Заметки на будущее
# Передать несколько переменых и произвести вычисления
# Передать несколько символов,  сформировать словарь и произвести манипуляции со словарем используя возможности Python

