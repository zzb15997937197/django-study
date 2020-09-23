from django.urls import path

from . import views
from polls.user import InsertUser, SelectUser, UserLogin, UserLogout, MyClassInfo, ChageUserInfo, BatchCreateUser
from polls.date import Test01, Test02, Test03
from polls.python_study.reportlab_pdf_demo_2 import some_view

urlpatterns = [
    # ex: polls
    # name属性可以随意取
    path('', views.index, name='index'),
    path('insert/record/<name>', InsertUser.as_view()),
    path('batch/create/<uid>', BatchCreateUser.as_view()),
    path('get/records/<uuid>', SelectUser.as_view()),
    path('login', UserLogin.as_view()),
    path('logout', UserLogout.as_view()),
    path('get/class/info/<uid>', MyClassInfo.as_view()),
    path('hello', views.hello, name='hello'),
    # 根据用户名来查询用户
    path('get/user/by/username', views.my_custom_sql),
    # 根据用户名模糊匹配到用户
    path('get/user/by/username/<username>', views.get_user_by_username),
    # 测试事务的使用
    path('change/data/<uid>', ChageUserInfo.as_view()),
    # 计算日期
    path('count/date', Test01.as_view()),
    # 查看目录
    path('get/dir/<uid>', Test02.as_view()),
    path('get/dir1/<uid>', Test03.as_view()),
    # 获取用户信息，测试choices
    path('get/user', views.get_user_info),
    # 生成pdf文件
    path('produce/pdf', some_view, name="pdf_view")

]
