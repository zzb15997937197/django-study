from django.db import models

# Create your models here.

# 以下的UserTest会生成一个myapp_usertest表
class User(models.Model):
     username=models.CharField(max_length=20,verbose_name="用户名",null=True)
     password=models.CharField(max_length=20,verbose_name="密码",null=True)
     def __str__(self):
         return "用户测试表"