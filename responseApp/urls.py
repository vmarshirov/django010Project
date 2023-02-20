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

app_name = "responseApp"
urlpatterns = [
    path("", views.index),
    path("html/", views.html),
    path("f_str/<str:str_value>", views.f_str),
    path("f_int/<int:int_value>", views.f_int),
    path("f_slug/<slug:slug_value>", views.f_slug),
    path("f_str_int_slug/<str:str_value>/<int:int_value>/<slug:slug_value>", views.f_str_int_slug),
    path("f_path/<path:path_value>", views.f_path),
]
