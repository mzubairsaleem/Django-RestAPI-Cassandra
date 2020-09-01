"""boardmaster357 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp import views

urlpatterns = [
    path('products/', views.overview, name="overview"),
    path('products/list/', views.get, name="list"),
    path('products/detail/<str:key>/', views.get_one, name="detail"),
    path('products/create/', views.post, name="create"),
    path('products/create_list/', views.post_list, name="create"),
    path('products/update/<str:key>/', views.update, name="update"),
    path('products/delete/<str:key>/', views.delete, name="delete"),

    path('attributes/', views.attributes_overview, name="attributes_overview"),
    path('attributes/list/', views.attributes_get, name="attributes_list"),
    path('attributes/detail/<str:key>/', views.attributes_get_one, name="attributes_detail"),
    path('attributes/create/', views.attributes_post, name="attributes_create"),
    path('attributes/update/<str:key>/', views.attributes_update, name="attributes_update"),
    path('attributes/delete/<str:key>/', views.attributes_delete, name="attributes_delete"),
]
