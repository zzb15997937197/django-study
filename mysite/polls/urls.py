from django.urls import path

from . import views
from polls.user import InsertUser, SelectUser, UserLogin, UserLogout, MyClassInfo

urlpatterns = [
    # ex: polls
    # name属性可以随意取
    path('', views.index, name='index'),
    path('<int:q_id>/', views.detail, name='detail'),
    path('<int:q_id>/result', views.result, name='result'),
    path('insert/record/<name>', InsertUser.as_view()),
    path('get/records', SelectUser.as_view()),
    path('login', UserLogin.as_view()),
    path('logout', UserLogout.as_view()),
    path('get/class/info/<uid>', MyClassInfo.as_view())

]
