from django.urls import path

from . import views
from polls.user import InsertUser

urlpatterns = [
    #name属性可以随意取
    path(r'index', views.index, name='index'),
    path(r'insert/record/<name>',InsertUser.as_view())
]