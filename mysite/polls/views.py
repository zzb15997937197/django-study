from django.shortcuts import render

# Create your views here.返回给前端页面

from django.http import HttpResponse


def index(request):
    return HttpResponse("hello word,you are at the poll index")


# 编写三个视图，Detail,result,note
def detail(request, q_id):
    return HttpResponse("you are looking at question %s" % q_id)


def result(request, q_id):
    return HttpResponse("you are looking at question %s" % q_id)
