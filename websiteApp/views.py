from django.shortcuts import render
from .forms import AbcForm
from django.http import HttpResponse

def home(request):
    print("home")
    last_url_element = last_url_elemen(request)
    return render(request, "home.html", {"last_url_element":last_url_element})

def last_url_elemen(request):
    url_elements_list = request.path.split("/")
    print("url_elements_list: ", url_elements_list)
    print("last_url_element: ", url_elements_list[-2])
    return ( url_elements_list[-2])



def form_get_all(request):
    last_url_element = last_url_elemen(request)

    print("\n\nrequest.GET\n", request.GET)
    print('\n\ndir(request.GET)\n',dir(request.GET))

    keys_list = list(request.GET.keys())
    print("\n\nkeys_list\n", keys_list)

    values_list = list(request.GET.values())
    print("\n\nvalues_list\n", values_list)

    items_dict = dict(request.GET.items())
    print("\n\n items_dict \n", items_dict)

    print("\n\nprn:\n",request.GET.getlist)
    
    context = {'items_dict': items_dict, 'last_url_element':last_url_element}
    return render(request, 'context.html', context) 

    # return HttpResponse(f"""
    # {values_list}
    # </pre>
    # """)


def form_abc(request):
    last_url_element = last_url_elemen(request)
    # <div id="pk">{{ last_url_element }}</div>
    context = {'last_url_element':last_url_element}
    return render(request, "form_abc.html", context)


def solution(a, b, c):
    if a + b == c:   result = " С равна сумме A и B"
    else:   result = "С не равна сумме A и B"
    return result   

 
def abc_form_get(request):
    last_url_element = last_url_elemen(request)
    form = AbcForm(request.GET)
    if form.is_valid():
        print("\n\nform is valid")
        # form =  AbcForm(initial={"c": 0})
        print(form)
        form_dict = form.cleaned_data
        print(form_dict)
        a = form_dict['a']
        b = form_dict['b']
        c = form_dict['c']
        print("a,b,c:", a,b,c)
        result = solution(a, b, c) 
        context = {'form_get': form, 'result': result, 'last_url_element':last_url_element}
        return render(request, 'abc_form_get.html', context)
    else: 
        print("\n\nform is not valid")
        form = AbcForm()
        context = {'form_get': form, 'last_url_element':last_url_element}
        return render(request, 'abc_form_get.html', context) 


def abc_form_post(request):
    last_url_element = last_url_elemen(request)
    if request.method == "POST":
        form = AbcForm(request.POST)
        print(form)
        if form.is_valid():
            print("\n\nform valid")
            # form =  AbcForm(initial={"c": 0})
            print(form)
            form_dict = form.cleaned_data
            print(form_dict)
            a = form_dict['a']
            b = form_dict['b']
            c = form_dict['c']
            print("a,b,c:", a,b,c)
            result = solution(a, b, c) 
            context = {'form': form, 'result': result, 'last_url_element':last_url_element}
            return render(request, 'abc_form_post.html', context) 
    else:
        form = AbcForm()
        print(form)
        context = {'form': form, 'last_url_element':last_url_element}
        return render(request, 'abc_form_post.html', context) 






def store(request):
    last_url_element = last_url_elemen(request)
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
    context = {'last_url_element':last_url_element,
               'dict_of_array': dict_of_array}
    print(context)
    return render(request, "store.html", context)

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
    return render(request, "store_result.html", {'d':d})
