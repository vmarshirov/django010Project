from django.shortcuts import render






# Create your views here.

# def index(request)
#     return HttpResponse('renderApp')


def index(request): # http://127.0.0.1:8000/renderApp/
    return render(request, "renderApp/index.html")


def greet(request, name): # http://127.0.0.1:8000/renderApp/greet/Иванов
    return render(request, "renderApp/greet.html", {"name": name})


def page_01(request, query_str): # http://127.0.0.1:8000/renderApp/page_01
    print(request)
    print(query_str)

    return render(request, "renderApp/page_01.html", {"queryStr": query_str})
