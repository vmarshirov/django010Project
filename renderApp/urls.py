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

app_name = "renderApp"
urlpatterns = [
    path("", views.index, name="index"),
    path("greet/<str:value>", views.greet, name="greet"),
    path("page_01/<path:path_value>", views.page_01, name="page_01"),
    path("page_02/<path:path_value>", views.page_02, name="page_02"),
    path("pages/<path:path_value>", views.pages, name="pages"),
    path("task/<path:path_value>", views.task, name="task"),
    path("objects_arrays/", views.objects_arrays, name="objects_arrays"),
]
