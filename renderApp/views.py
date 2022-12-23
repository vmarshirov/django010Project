from django.http import HttpResponse
from django.shortcuts import render


# http://127.0.0.1:8000/renderApp/
# http://127.0.0.1:8000/renderApp/greet/Иванов


# Create your views here.

# def index(request)
#     return HttpResponse('renderApp')


def index(request):
    return render(request, "renderApp/index.html")


def greet(request, name):
    return render(request, "renderApp/greet.html", {"name": name})


def page_01(request):
    return render(request, "renderApp/page_01.html")
