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
    a_value = int(request_path_elements[path_len - 1])
    print ("a_value: ", a_value)
    if a_value > 0:  result_value = "a > 0"
    else: result_value = "a <= 0"

    context = {
        "formulation_value": formulation_value,
        "a_value": a_value,
        "result_value": result_value
    }
    print ("context: ",context) 
    return render(request, "task.html", context)


def store(request):
    
    objects_array = [
        {
            "id": "1",
            "title": "Товар 1",
            "vendor_code": "VC111",
            "description": "Описание 1",
            "price": 100,
            "img": "/images/uso_001.jpg"
        },
        {
            "id": "2",
            "title": "Товар 2",
            "vendor_code": "VC222",
            "description": "Описание 2",
            "price": 200,
            "img": "/images/uso_002.jpg"
        },
        {
            "id": "3",
            "title": "Товар 3",
            "vendor_code": "VC333",
            "description": "Описание 3",
            "price": 300,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg"
        },
        {
            "id": "4",
            "title": "Товар 4",
            "vendor_code": "VC444",
            "description": "Описание 4",
            "price": 400,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_004.jpg"
        }
    ]
    dict_of_array = {'objects_array': objects_array}
    context = {'dict_of_array': dict_of_array}
    print(context)
    return render(request, "store.html", context)