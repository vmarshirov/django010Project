from django.shortcuts import render

# https://docs.djangoproject.com/en/4.1/topics/templates/
# https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#id3
# https://docs.djangoproject.com/en/4.1/ref/templates/language/


def index(request): # http://127.0.0.1:8000/renderApp/
    return render(request, "renderApp/index.html")


def greet(request, name): # http://127.0.0.1:8000/renderApp/greet/Иванов
    return render(request, "renderApp/greet.html", {"name": name})

def page_01(request, query_str): # http://127.0.0.1:8000/renderApp/page_01
    print(request)
    print(query_str)
    context = {"query_str": query_str}
    return render(request, "renderApp/page_01.html",context)
    # return render(request, "renderApp/page_01.html", {"query_str": query_str})
