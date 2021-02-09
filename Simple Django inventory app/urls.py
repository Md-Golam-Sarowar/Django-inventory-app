"""DjangoTodoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from todoApp.views import HomePage, itemDetailsView
from todoApp.views import addItem, deleteItem, updateItem, updateItemPage


urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", HomePage),
    path("addTodo/", addItem),
    path("deleteTodo/<int:item_id>/", deleteItem),
    path("updateItem/<int:item_id>/", updateItem),
    path("updateItemPage/", updateItemPage),
    path("itemDetails/<int:item_id>/", itemDetailsView),
]
