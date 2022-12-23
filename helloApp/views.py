from django.http import HttpResponse


# from django.shortcuts import render

# Create your views here.

# http://127.0.0.1:8000/helloApp/
# http://127.0.0.1:8000/helloApp/abc/
# http://127.0.0.1:8000/helloApp/f_str/abc
# http://127.0.0.1:8000/helloApp/f_int/12345
# http://127.0.0.1:8000/helloApp/f_slug/building-your-1st-django-site
# http://127.0.0.1:8000/helloApp/f_path/12345

def index(request):
    return HttpResponse("helloApp")


def abc(request):
    return HttpResponse("abc")


def f_str(request, str_value):
    print("type(request), request: ", type(request), request)
    print("type(str_value), str_value: ", type(str_value), str_value)
    return HttpResponse(f"f_str, str_value.capitalize():  {str_value.capitalize()}")


def f_int(request, int_value):
    print(type(int_value), int_value)
    return HttpResponse(f"f_int, int_value: {int_value}")


def f_slug(request, slug_value):
    print(type(slug_value), slug_value)
    return HttpResponse(f"f_slug, slug_value: {slug_value}")


def f_path(request, path_value):
    print(type(path_value), path_value)
    return HttpResponse(f"f_path, path_value: {path_value}")
