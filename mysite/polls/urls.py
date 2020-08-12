from django.urls import path

from . import views
from polls.user import InsertUser, SelectUser, UserLogin, UserLogout

urlpatterns = [
    # name属性可以随意取
    path(r'index', views.index, name='index'),
    path(r'insert/record/<name>', InsertUser.as_view()),
    path(r'select/all/record/<uuid>', SelectUser.as_view()),
    path(r'login', UserLogin.as_view()),
    path(r'logout', UserLogout.as_view())
]
