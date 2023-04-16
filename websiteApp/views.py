from django.shortcuts import render
from django import forms
from django.http import HttpResponse


def def_url_elements(request):
    url_elements_list = request.path.split("/")
    print("url_elements_list: ", url_elements_list)
    print("last_url_element: ", url_elements_list[-2])
    return ({"last_url_element": url_elements_list[-2]})


def index(request):
    last_url_element = def_url_elements(request)
    return render(request, "websiteApp/index.html", last_url_element)


def home(request):
    last_url_element = {"last_url_element": 'home'}
    return render(request, "websiteApp/home.html", last_url_element)


def form(request):
    last_url_element = def_url_elements(request)
    return render(request, "websiteApp/form.html", last_url_element)



class AbcFormCreate(forms.Form):
    a = forms.IntegerField(initial=1, min_value=2)
    b = forms.IntegerField(required=False)
    c = forms.IntegerField(label='c_lable' )

def form_create(request):
    last_url_element = def_url_elements(request)
    abc_form = AbcFormCreate()
    print(abc_form)
    context = {'last_url_element': last_url_element,
               'abc_form': abc_form}
    return render(request, 'websiteApp/form_create.html', context)

def form_get(request):
    print(request.GET)
    print(request.GET.get("a"))
    print(request.GET.get("b"))
    print(request.GET.get("c"))
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    abc_obj={"a":a, "b":b, "c":c}
    return HttpResponse(f"""
    <pre>
    a = {a}
    b = {b}
    c = {c}
    abc_obj = {abc_obj}
    a_abc_obj = {abc_obj['a']}
    </pre>
    """)

def form_get_all(request):
    print(request.GET)
    r = list(request.GET.values())
    return HttpResponse(f"""
    <pre> См. терминал 
    {r}
    </pre>
    """)


def form_abc(request):
    last_url_element = def_url_elements(request)
    return render(request, "websiteApp/form_abc.html", last_url_element)

def store(request):
    last_url_element = def_url_elements(request)
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
    context = {'urls': last_url_element,
               'dict_of_array': dict_of_array}
    print(context)
    return render(request, "websiteApp/store.html", context)

def store_result(request): # http://127.0.0.1:8000/renderApp/greet/Иванов
    print(request.__dir__())
    req = dict(request.GET)
    print (req)
    vendor_code = req.get("vendor_code")
    amount = req.get("amount")
    print(vendor_code, amount)
    i=0
    d = {}
    for key in vendor_code:
        print(vendor_code[i], amount[i])
        d[vendor_code[i]] = amount[i]
        i+=1
    print(d)
    return render(request, "websiteApp/store_result.html", {'d':d})
