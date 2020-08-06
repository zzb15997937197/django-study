from django.http import HttpResponse
from requests import Response
from rest_framework.views import APIView

from polls.models import User


class InsertUser(APIView):
    def get_or_create(self, request,name):
        print("插入一名员工!")
        # 1.怎么获取数据库对象
        b=User(username=name,password="123456")
        b.save()
        b.username="bingbing"
        b.save()
        ## do something
        print("插入完毕!")
        return HttpResponse("Some data")

    def get(self, request,name):
        return self.get_or_create(request,name)

    def post(self, request,name):
        return self.get_or_create(request,name)


class SelectUser(APIView):
    def get(self,request):
        print("查询员工信息!")
        user=User.objects.all().values_list("username","password")
        print(user)
        print("查询完毕!")
        return HttpResponse(user)