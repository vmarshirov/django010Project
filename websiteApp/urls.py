"""django010Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = "websiteApp"
urlpatterns = [
    path("", views.home),
    path("home/", views.home, name="home"),
    path("form_abc/", views.form_abc, name="form_abc"),
    path("abc_form_get/", views.abc_form_get, name="abc_form_get"),
    path("abc_form_post/", views.abc_form_post, name="abc_form_post"),
    path("form_get_all/", views.form_get_all,  name="form_get_all"),
    path("store/", views.store, name="store"),
    path("store_result/", views.store_result, name="store_result"),
    # path("page_01/<path:queryStr>", views.page_01, name="websiteApp-page_01"),
]
