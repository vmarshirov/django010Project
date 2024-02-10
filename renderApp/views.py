from django.shortcuts import render, redirect

# https://docs.djangoproject.com/en/4.1/topics/templates/
# https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#id3
# https://docs.djangoproject.com/en/4.1/ref/templates/language/
# https://docs.python.org/3/library/stdtypes.html#index-51


def index(request):  # http://127.0.0.1:8000/renderApp/
    return render(request, "index.html")


def greet(request, value):  # http://127.0.0.1:8000/renderApp/greet/Иванов
    print(value)
    print(request.__dir__())
    print(request.GET)
    return render(request, "greet.html", {"key": value})


def page_01(request, path_value):  # http://127.0.0.1:8000/renderApp/page_01/id/page/010
    print(path_value)
    print(request.path)
    context = {"path_value": path_value}
    return render(request, "page_01.html", context)


def page_02(request, path_value):  # http://127.0.0.1:8000/renderApp/page_02/id/page/020
    print(path_value)
    print(request.path)
    context = {"path_value": path_value}
    return render(request, "page_02.html", context)


def pages(request, path_value):  # http://127.0.0.1:8000/renderApp/pages/01
    print(path_value)
    print(request.path)
    context = {"path_value": path_value}
    if path_value == "first":
        return render(request, "page_01.html", context)
    elif path_value == "second":
        return render(request, "page_02.html", context)
    # else: return redirect("renderApp:index")
    else:
        return redirect("renderApp:page_01", path_value)


def task(request, path_value):
    print(path_value)
    print("request.path: ", request.path)
    request_path_elements = request.path.split("/")
    print("request_path_elements:", request_path_elements)
    print("request_path_elements.__len__():", request_path_elements.__len__())
    path_len = request_path_elements.__len__()
    formulation_value = request_path_elements[path_len - 2]
    a_value = request_path_elements[path_len - 1]
    context = {
        "formulation_value": formulation_value,
        "a_value": a_value,
        "result_value": "result_value",
    }
    return render(request, "task.html", context)
