from django.shortcuts import render


def def_path_element(request):
    path_elements = request.path.split("/")
    print("path_elements: ", path_elements)
    elements_amount = path_elements.__len__()
    print("elements_amount: ", elements_amount)
    path_element = path_elements[elements_amount - 1]
    print("path_element: ", path_element)
    return ({"path_element": path_element})


def index(request):
    path_element = def_path_element(request)
    return render(request, "websiteApp/index.html", path_element)


def home(request):
    path_element = def_path_element(request)
    return render(request, "websiteApp/home.html", path_element)


def form(request):
    path_element = def_path_element(request)
    return render(request, "websiteApp/form.html", path_element)


def form_abc(request):
    path_element = def_path_element(request)
    return render(request, "websiteApp/form_abc.html", path_element)


def store(request):
    path_element = def_path_element(request)
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
            "img": "https://raw.githubusercontent.com/vmarshirov/g06u28/main/images/uso_003.jpg"
        }
    ]
    objects_array ={'objects_array': objects_array}
    content = {'path_element': path_element,'objects_array': objects_array}
    print(content)
    return render(request, "websiteApp/store.html", content)
