from django.shortcuts import render, redirect

# https://docs.djangoproject.com/en/4.1/topics/templates/
# https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#id3
# https://docs.djangoproject.com/en/4.1/ref/templates/language/
# https://docs.python.org/3/library/stdtypes.html#index-51


""" def index(request):  # http://127.0.0.1:8000/renderApp/
    return render(request, "index.html")
 """

def index(request):  # http://127.0.0.1:8000/renderApp/greet/Иванов
    path_value = "Привет"
    return render(request, "greet.html", {"key": path_value})

def greet(request, path_value):  # http://127.0.0.1:8000/renderApp/greet/Иванов
    print(path_value)
    context = {"key": path_value}
    return render(request, "greet.html", context)


def page_01(request, path_value):  # http://127.0.0.1:8000/renderApp/page_01/id/page/010
    print("path_value: ", path_value)
    print(request.path)
    context = {"path_value": path_value}
    return render(request, "page_01.html", context)


def page_02(request, path_value):  # http://127.0.0.1:8000/renderApp/page_02/id/page/020
    print("path_value: ", path_value)
    print(request.path)
    context = {"path_value": path_value}
    return render(request, "page_02.html", context)


def pages(request, path_value):  # http://127.0.0.1:8000/renderApp/pages/01
    print("path_value: ", path_value)
    print(request.path)
    context = {"path_value": path_value}
    if path_value == "first":
        return render(request, "page_01.html", context)
    elif path_value == "second":
        return render(request, "page_02.html", context)
    # else: return redirect("renderApp:index")
    else:
        return redirect("renderApp:page_01", path_value)

def task_solution(a_value):
    if a_value > 0:
        result_value = "a > 0"
    else:
        result_value = "a <= 0"
    return result_value

def task(request, path_value):
    print("path_value: ", path_value)
    #print("request.path: ", request.path)
    path_elements = path_value.split("/")
    print ("path_elements: ", path_elements)
    list_a =  path_elements[0].split("=")
    int_a = int(list_a[1])
    print("int_a: ", int_a)
    result_value = task_solution(int_a)
    formulation_value = "2001. Значение переменной  а больше нуля ?"
    context = {
        "formulation_value": formulation_value,
        "a_value": int_a,
        "result_value": result_value,
    }
    print("context: ", context)
    return render(request, "task.html", context)


def objects_arrays(request):
    goods_array = [
        {
            "id": "1",
            "title": "Товар 1",
            "vendor_code": "VC111",
            "description": "Описание 1",
            "price": 100,
            "img": "renderApp/images/uso_001.jpg",
        },
        {
            "id": "2",
            "title": "Товар 2",
            "vendor_code": "VC222",
            "description": "Описание 2",
            "price": 200,
            "img": "renderApp/images/uso_002.jpg",
        },
        {
            "id": "3",
            "title": "Товар 3",
            "vendor_code": "VC333",
            "description": "Описание 3",
            "price": 300,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg",
        },
        {
            "id": "4",
            "title": "Товар 4",
            "vendor_code": "VC444",
            "description": "Описание 4",
            "price": 400,
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_004.jpg",
        },
    ]

    box_array = [
        {"title": "Название 1", "description": "Описание 1", "img": "renderApp/images/1_1.png"},
        {"title": "Название 2", "description": "Описание 2", "img": "renderApp/images/1_2.png"},
    ]
    print("goods_array: " ,goods_array)
    print ("box_array: ", box_array)
    dict_of_array = {"goods_array": goods_array, "box_array": box_array}
    context = {"dict_of_array": dict_of_array}
    print("context: ", context)
    return render(request, "objects_arrays.html", context)
