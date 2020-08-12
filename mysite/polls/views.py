from django.shortcuts import render

# Create your views here.返回给前端页面

from django.http import HttpResponse
def index(request):
    return HttpResponse("hello word,you are at the poll index")