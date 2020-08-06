from django.db import models

# Create your models here.

# 以下的UserTest会生成一个myapp_usertest表，在Meta类里添加表的信息。
class User(models.Model):
     username=models.CharField(max_length=20,verbose_name="用户名",null=True)
     password=models.CharField(max_length=20,verbose_name="密码",null=True)
     def __str__(self):
         return "用户测试表"

     class Meta:
         verbose_name="用户表"
         verbose_name_plural="用户表"
         db_table="sys_user"


class Blog(models.Model):
    name=models.CharField(max_length=100)
    tagline=models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    def __str__(self):
        return self.headline