from django.http import HttpResponse
from rest_framework.views import APIView
from polls.HttpResult import Result
from polls.models import User, MyClassReource
from django.http import JsonResponse
from polls.BaseView import BaseView
from django.db import transaction, connection
from django.db.models import Aggregate, Avg, Count, Sum, Max, Min

from polls.serializers import UserSerializers


class BatchCreateUser(APIView):

    def post(self, request, uid=None):
        b = User(username=uid)
        q = []
        for i in range(0, 10):
            q.append(b)
        users = User.objects.bulk_create(q)
        print(users)
        return HttpResponse("批量创建对象!")


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


class ChageUserInfo(BaseView):

    # 要么全部成功，要么全部失败
    @transaction.atomic
    def put(self, request, uid=None):
        r = Result()
        a = 1
        try:
            # 开启事务
            tid = transaction.savepoint()
            user = User(id=uid)
            user.username = "bingbing"
            user.save()
            raise Exception("出错了!")
            transaction.savepoint_commit(tid)
        except Exception as e:
            transaction.savepoint_rollback(tid)
            r.error(e)
        return self.s_result(r)


class SelectUser(APIView):
    def get(self, request, uuid):
        print("查询员工信息!")
        # values返回的是一个字典
        user = User.objects.all().values("username", "password")
        print(user)
        # 使用filter,类似于Mysql的where子句
        # values_list()返回成为元组
        user1 = User.objects.all().filter(username="zhuzhu").values_list("password")
        print("user1", user1)
        # .exclude  排除
        user2 = User.objects.all().exclude(username="zhuzhu").values_list("username", "password")
        print("user2", user2)
        one_entry = User.objects.get(pk=1)
        print(one_entry)
        print("查询完毕!")
        # 打印sql
        print("sql:", connection.queries)
        return HttpResponse(user)

# 登入
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
            print("找到记录:", result)
            # 当前登录的result为User对象里的信息
            # 序列化的时候此处必须要传result,否则序列化后的结果为""
            r.data = UserSerializers(result).data
            print("序列化后的对象信息为:", r.data)
            ## {'id': 4, 'username': 'zhuzhu', 'password': '123456'}
            request.session['user'] = r.data
            print('dict一些信息:', self.__dict__)
        except Exception as e:
            r.error(e)
            return HttpResponse(e)
        return JsonResponse(r.data)


# 登出
class UserLogout(APIView):
    def post(self, request):
        # 先获取用户
        self.getuser(request)
        # 删除用户信息
        self.outuser(request)

    def getuser(self, request):
        if 'user' not in request.session:
            raise Exception('请先登录！')
            # 跳转到登录页面
        else:
            self.student = request.session['user']

    def outuser(self, request):
        del request.session['user']


## 查询我的班级信息
class MyClassInfo(APIView):
    def get(self, request, uid):
        r = Result()
        # 根据uid来获取到
        user = MyClassReource.objects.filter(id=uid).first()

        print(user)
        myClassReource = MyClassReource.objects.filter(id=uid)
        return HttpResponse("成功")
