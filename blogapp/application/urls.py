"""
URL configuration for blogapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from application import views
app_name='application'

urlpatterns = [
    path('appbase/',views.apphome,name='appbase'),
    path('create/',views.create,name='create'),
    path('search/',views.search,name='search'),
    path('read/<int:s>/',views.read,name='read'),
    path('bloglist/',views.bloglist,name='bloglist'),
    path('edit/<int:p>/',views.edit,name='edit'),
    path('delete/<int:p>/',views.deleteblog,name='delete')


]
