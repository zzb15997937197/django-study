from django.http import HttpResponse
from requests import Response
from rest_framework.views import APIView


class InsertUser(APIView):

    def get_or_create(self, request):
        print("插入一名员工!")
        ## do something
        print("插入完毕!")
        return HttpResponse("Some data")

    def get(self, request):
        return self.get_or_create(request)

    def post(self, request):
        return self.get_or_create(request)
