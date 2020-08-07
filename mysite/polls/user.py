from django.http import HttpResponse
from requests import Response
from rest_framework.views import APIView
from polls.HttpResult import Result
from polls.models import User
from rest_framework import serializers
from django.http import JsonResponse


class InsertUser(APIView):
    def get_or_create(self, request, name):
        print("插入一名员工!")
        # 1.怎么获取数据库对象
        b = User(username=name, password="123456")
        b.save()
        b.username = "bingbing"
        b.save()
        ## do something
        print("插入完毕!")
        return HttpResponse("Some data")

    def get(self, request, name):
        return self.get_or_create(request, name)

    def post(self, request, name):
        return self.get_or_create(request, name)


class SelectUser(APIView):
    def get(self, request):
        print("查询员工信息!")
        user = User.objects.all().values_list("username", "password")
        print(user)
        # 使用filter,类似于Mysql的where子句
        user1 = User.objects.all().filter(username="猪猪").values_list("password")
        print(user1)
        # .exclude  排除
        user2 = User.objects.all().exclude(username="猪猪").values_list("username", "password")
        print(user2)
        one_entry = User.objects.get(pk=1)
        print(one_entry)
        print("查询完毕!")
        return HttpResponse(user)


# 登入
class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password")


class UserLogin(APIView):

    @staticmethod
    def s_result(result):
        r = result.to_json_string()
        return JsonResponse(result.__dict__,
                            json_dumps_params={'sort_keys': False, 'indent': 4, 'ensure_ascii': False}, safe=False)

    def post(self, request):
        r = Result()
        try:
            username = request.data["username"]
            password = request.data["password"]
            result = User.objects.filter(username=username, password=password).first()
            if result is None:
                print("出错了!")
                raise Exception("用户名或密码错误!")

            # 否则登录成功, 在赋值给session之前需要先将result转换为json串，否则报错:TypeError: Object of type User is not JSON serializable
            # request.session['user'] = result
            # print(request.session['user'])
            r.data = UserSerialize(result).data
            print("序列化后的对象信息为:", r.data)
            ## {'id': 4, 'username': 'zhuzhu', 'password': '123456'}
            request.session['user'] = r.data
            print('dict一些信息:', self.__dict__)
        except Exception as e:
            r.error(e)
            return HttpResponse(e)
        return self.s_result(r)


# 登出
class UserLogout(APIView):
    def post(self, request):
        # 先获取用户
        self.getuser(request)
        # 删除用户信息
        self.outuser(request)

    def getuser(self, request):
        if 'student' not in request.session:
            raise Exception('请先登录！')
            # 跳转到登录页面
        else:
            self.student = request.session['student']

    def outuser(self, request):
        del request.session['user']
