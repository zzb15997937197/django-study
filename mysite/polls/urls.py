from django.urls import path

from . import views
from polls.user import InsertUser, SelectUser, UserLogin, UserLogout, MyClassInfo

urlpatterns = [
    # ex: polls
    # name属性可以随意取
    path('', views.index, name='index'),
    path('insert/record/<name>', InsertUser.as_view()),
    path('get/records/<uuid>', SelectUser.as_view()),
    path('login', UserLogin.as_view()),
    path('logout', UserLogout.as_view()),
    path('get/class/info/<uid>', MyClassInfo.as_view()),
    path('hello', views.hello, name='hello'),
    #根据用户名来查询用户
    path('get/user/by/username',views.my_custom_sql)

]
