from django.contrib import admin
from polls.models import User


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ("username", "password")


## 注册到admin用户里
admin.site.register(User, UserAdmin)

##自定义主题
admin.site.site_header = "学生管理系统"
admin.site.site_title = "学生管理系统"
admin.site.index_title = "学生管理系统"
