"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
import blog.views


urlpatterns = [
    path('admin/', admin.site.urls),
    # read
    path('',blog.views.home, name = "home"),
    path('blog/<int:id>',blog.views.detail,name="detail"),
    #create
    path('new',blog.views.new,name = 'new'),
    path('create',blog.views.create, name = 'create'),
    # update 
    path('blog/edit/<int:id>',blog.views.edit,name="edit"),
    path('blog/update/<int:id>',blog.views.update,name="update"),
    #deleate
    path('blog/delete/<int:id>',blog.views.delete, name = "delete")
]
