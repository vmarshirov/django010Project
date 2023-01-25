from django.shortcuts import render


def def_path_element(request):
    path_elements = request.path.split("/")
    print("path_elements: ", path_elements)
    elements_amount = path_elements.__len__()
    print("elements_amount: ", elements_amount)
    path_element = path_elements[elements_amount - 1]
    print("path_element: ", path_element)
    return (path_element)


def index(request):
    path_element = def_path_element(request)
    return render(request, "AppStaticSite/index.html", context={"path_element": path_element})


def home(request):
    path_element = def_path_element(request)
    return render(request, "AppStaticSite/home.html", context={"path_element": path_element})


def form(request):
    path_element = def_path_element(request)
    return render(request, "AppStaticSite/form.html", context={"path_element": path_element})


def form_abc(request):
    path_element = def_path_element(request)
    return render(request, "AppStaticSite/form_abc.html", context={"path_element": path_element})
