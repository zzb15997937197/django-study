from django.shortcuts import render

# Create your views here.返回给前端页面
from django.http import HttpResponse, JsonResponse
from polls.HttpResult import Result
from django.db import connection
from polls.models import Student
from polls.serializers import StudentSerializers
from polls.models import EDUCATION_CHOICE
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


def get_user_by_username(request, username=None):
    r = Result()
    student = Student.objects.get(name__icontains=username)
    print(student)
    return HttpResponse("success")


def get_user_info(request):
    student = Student.objects.all()
    datas = []
    for i in student:
        data = StudentSerializers(i).data
        g = i.gender
        gender_name = EDUCATION_CHOICE(g)
        datas.append(data)
    return JsonResponse(datas, safe=False)
