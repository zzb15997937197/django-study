from django.urls import path

from . import views
from polls.user import InsertUser

urlpatterns = [
    #name属性可以随意取
    path('index', views.index, name='index'),
    path('insert/record',InsertUser.as_view())
]