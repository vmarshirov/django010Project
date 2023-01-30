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
    context = def_path_element(request)
    return render(request, "websiteApp/index.html", context)


def home(request):
    context = def_path_element(request)
    return render(request, "websiteApp/home.html", context)


def form(request):
    context = def_path_element(request)
    return render(request, "websiteApp/form.html", context)


def form_abc(request):
    context = def_path_element(request)
    return render(request, "websiteApp/form_abc.html", context)
