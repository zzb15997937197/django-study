from django.shortcuts import render

# Create your views here.返回给前端页面
import datetime
from django.template.loader import get_template
from django.template.context import Context
from django.http import HttpResponse, JsonResponse
from polls.HttpResult import Result
from django.db import connection
from polls.Serializers import UserSerializers

from django.shortcuts import render, render_to_response, redirect


def index(request):
    return HttpResponse("hello word,you are at the poll index")


def hello(request):
    return render(request, "hello.html")


def my_custom_sql(request):
    r = Result()
    username = request.GET.get("username")
    with connection.cursor() as cursor:
        cursor.execute("select * from sys_user where username=%s", [username])
        cursor.execute("select * from auth_user")
        row = cursor.fetchall()
        print("row", row)
    return HttpResponse(row)
