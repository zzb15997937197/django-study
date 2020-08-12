from django.shortcuts import render

# Create your views here.返回给前端页面
import datetime
from django.template.loader import get_template
from django.template.context import Context
from django.http import HttpResponse

from django.shortcuts import render, render_to_response, redirect


def index(request):
    return HttpResponse("hello word,you are at the poll index")


def hello(request):
    return render(request, "hello.html")
