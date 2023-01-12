from django.http import HttpResponse
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

#
# def f_str(request, str_value):
#     print("type(request), request: ", type(request), request.path)
#     print("request.META:", request.META.get("HTTP_HOST"))
#     path_elements = request.path.split("/")
#     elements_amount = path_elements.__len__()
#     path_element = path_elements[elements_amount - 2]
#     print("type(str_value), str_value: ", type(str_value), str_value)
#     return HttpResponse(
#         f"<p>f_str, str_value.capitalize():  {str_value.capitalize()}; \n<br>path_element: {path_element} \n</p>")
#
#
# def f_int(request, int_value):
#     print(type(int_value), int_value)
#     return HttpResponse(f"f_int, int_value: {int_value} ")
#
#
# def f_slug(request, slug_value):
#     print(type(slug_value), slug_value)
#     return HttpResponse(f"f_slug, slug_value: {slug_value}")
#
#
# def f_path(request, path_value):
#     print(type(path_value), path_value)
#     return HttpResponse(f"f_path, path_value: {path_value}")
