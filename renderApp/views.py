from django.shortcuts import render

# https://docs.djangoproject.com/en/4.1/topics/templates/
# https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#id3
# https://docs.djangoproject.com/en/4.1/ref/templates/language/
# https://docs.python.org/3/library/stdtypes.html#index-51

def index(request): # http://127.0.0.1:8000/renderApp/
    return render(request, "renderApp/index.html")


def greet(request, name): # http://127.0.0.1:8000/renderApp/greet/Иванов
    return render(request, "renderApp/greet.html", {"name": name})

def page_01(request, path_value): # http://127.0.0.1:8000/renderApp/page_01/id/page/010
    print(path_value)
    print(request.path)
    context = {"path_value": path_value}
    return render(request, "renderApp/page_01.html",context)

def page_02(request, path_value): # http://127.0.0.1:8000/renderApp/page_02/id/page/020
    print(path_value)
    print(request.path)
    context = {"path_value": path_value}
    return render(request, "renderApp/page_02.html",context)


