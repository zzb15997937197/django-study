1. 序列化时，class Meta: 下的model 可以为多个Model嘛？
   不可以，只能有一个model。
   如果是一对多的模式，可以直接使用直接序列关联的外键。 detail为关联的外键的model
    detail = DeitalSerializer()
   如果是多对多的模式，那么用serializers.SerializeMethodField()获取到一个新的对象schedule，
   然后再使用get_schedule方法来获取到所有的对象，obj.schedule.all()获取到所有班级对应的课程。
   然后对每一个schedule对象进行序列化。
       def get_schedule(self, obj):
        sch = obj.schedule.all()
        print("sch:",sch)
        ##sch: <TimestampQuerySet [<Schedule: 英语第一练>, <Schedule: 英语第一练>, <Schedule: 英语第一练>, <Schedule: 英语第一练>]>
        s = ScheduleSerializer(sch, many=True)
        return s.data

2. 怎么使用分页?
    使用django.core.paginator 下的paginator实现分页。



3. 怎么使用原生的sql执行数据库查询?
    可以直接在views.py文件里新建一个查询sql的方法，然后获取到参数后，再把结果拿出来即可:
    需要先导入一下包:
    from django.db import connection

    def my_custom_sql(request):
    username = request.GET.get("username")
    with connection.cursor() as cursor:
        cursor.execute("select * from sys_user where username=%s", [username])
        row = cursor.fetchone()
    return HttpResponse(row)

    使用with .. as ..
    sql执行完毕后，可以自动关闭数据库的连接。

    还有一种方式，你可以通过对象来执行原先的sql:
     for p in Person.objects.raw('SELECT * FROM myapp_person'):
...     print(p)


4. 启动时间报错：
   RuntimeWarning: DateTimeField SysClassDetail.fromTime received a naive datetime (2020-08-14 17:41:17.849080) whi
le time zone support is active.
   设置时区和USE_TZ=FALSE即可解决问题:
   TIME_ZONE = 'Asia/Shanghai'
  当 USE_TZ = True时，系统采用UTC时间；
  当 USE_TZ = False时，系统采用要看TIME_ZONE（时区）是否设置。若已设置时区，项目采用设置的时区的时间；若未设置，项目采用巴西时区的时间（utc-5），目前还不清楚为什么采用巴西的时区时间。


5. 索引
   在class Meta: 添加
   唯一性索引:  unique_together('first_name', 'last_name',)
   联合索引:  indexes = [
            # 联合索引，遵循mysql的最左匹配原则
            models.Index(fields=['last_name', 'first_name']),
            # 单个索引
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]


6.  怎么使用orm进行模糊查询
    通过使用name__icontains()属性即可。


7. 怎么在控制台上打印日志:

   LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level': 'DEBUG',
        },
    }
}


8. 选择数据库进行更新
    1) 更新
      my_object.save(using='legacy_users')

    2) 查询,可以选择默认的数据库，或者配置的admin数据库
       Author.objects.using('default').all()

9. 怎么在json里新增一条自定义的信息?
    可以直接通过r.v= value ,然后再转json串就行

10. 怎么给小数的结果取2位小数
    推荐使用方法: r.avg_score = ('%.1f' % (total / r.data_count / 3))


11. django怎么开启事务?
   from django.db import transaction
with transaction.atomic():
    ...

#第二种 装饰器
@transaction.atomic
    def post(self,request):
            ...
            sid=transaction.savepoint()  #开启事务
            ...
            transaction.savepoint_rollback(sid)  # 回滚
            ...
            transaction.savepoint_commit(sid)  # 提交

12. 怎么根据条件来进行查询?
     在url后拼接参数:
      http://bing.bojixt.com:8001/app/my/feedback/info/1?page=1&size=10&type_id=1

        # 根据类型来分类
        type_id = request.GET.get("type_id")
        if type_id is not None:
            feed_type = FeedBackType(id=type_id)
            feed_backs = Feedback.objects.all().filter(student_id=uid, delete_datetime=None, type=feed_type)
        else:
            feed_backs = Feedback.objects.all().filter(student_id=uid, delete_datetime=None)



13. 怎么让model不迁移到数据库里?
    不行，因为django会根据迁移文件，将model映射成数据库里的Sql。


14.  怎么计算日期?
    "2020-08-13T15:22:52"
     1. 字符串怎么转日期？

       已经解决！待整理
       使用timezone来计算2个日期的时间差！
       1) 在序列化的时候，要将获取出来的时间进行序列化操作，在序列化的时候通过str()方法,将日期转换为字符串。
       2)通过timezone下的datetime类来讲字符串日期转换为datetime
           datetime.strptime(s, '%Y-%m-%d'))  # 2019-01-20 00:00:00
       3）转换后的格式就相当于timezone.now()获取出来的时间。
       4) 通过比较时间戳来计算天数。
         import time

             @staticmethod
      def get_difference(start, end):
        start_time = start.strftime('%Y-%m-%d %H:%M:%S')
        end_time = end.strftime('%Y-%m-%d %H:%M:%S')
        now = time.strptime(start_time, '%Y-%m-%d %H:%M:%S')
        old = time.strptime(end_time, '%Y-%m-%d %H:%M:%S')
        # 转为时间戳后，时间戳相减
        delta_seconds = time.mktime(now) - time.mktime(old)
        return delta_seconds / 3600 / 24

        # 再讲时间戳，转换为时间
        # 注: 需要将时间转换为整数，然后再计算，要不然会报错不合法的参数
        print("delta_seconds",int(delta_seconds))
        timeArray = time.localtime(int(delta_seconds))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print("otherStyleTime",otherStyleTime)



15. 怎么将小数转换为整数，整数与小数互换？
      整数转换为小数:  rount(int,2)

16. filter怎么根据条件表达式来进行判断?
     比如  endTime-startTime>30 表示失效
           否则是有效的。

17. 判断变量类型的函数
 2 def typeof(variate):
 3     type=None
 4     if isinstance(variate,int):
 5         type = "int"
 6     elif isinstance(variate,str):
 7         type = "str"
 8     elif isinstance(variate,float):
 9         type = "float"
10     elif isinstance(variate,list):
11         type = "list"
12     elif isinstance(variate,tuple):
13         type = "tuple"
14     elif isinstance(variate,dict):
15         type = "dict"
16     elif isinstance(variate,set):
17         type = "set"
18     return type


17. 怎么序列化一个元组列表？
   <class 'tuple'>: ((1, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第一练', '美雅课程', 'meiya_niubi', 30), (2, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第二练', '美雅课程', 'meiya_niubi', 30), (3, 1, datetime.datetime(2020, 7, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第三练', '美雅课程', 'meiya_niubi', 30), (4, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第四练', '美雅课程', 'meiya_niubi', 30), (7, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第七练', '美雅课程', 'meiya_niubi', 30), (8, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第八练', '美雅课程', 'meiya_niubi', 30), (9, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第九练', '美雅课程', 'meiya_niubi', 30), (10, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第十练', '美雅课程', 'meiya_niubi', 30), (11, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第11练', '美雅课程', 'meiya_niubi', 30), (12, 1, datetime.datetime(2020, 8, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第12练', '美雅课程', 'meiya_niubi', 30), (13, 1, datetime.datetime(2020, 7, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第13练', '美雅课程', 'meiya_niubi', 30), (14, 1, datetime.datetime(2020, 7, 13, 15, 22, 52), datetime.datetime(2020, 8, 13, 15, 22, 50), None, '英语第14练', '美雅课程', 'meiya_niubi', 30))

  可以将元组单独拎出来，然后对每条数据进行初始化，可以先取出所有字段，然后一一对应。
   fields = Schedule._meta.fields
   for i in fields:
      print(i.name)

 18.RuntimeWarning: DateTimeField SysClassDetail.fromTime received a naive datetime (2020-08-13 13:54:05.865757) while time zone support is active.
  warnings.warn("DateTimeField %s received a naive datetime (%s)"  怎么解决？
     待解决

 10. 怎么对字典进行序列化?
       先可以给字典进行初始化:
       result_dict = {"data": dicts, "code": r.code, "msg": r.message, "total": total}
       然后再对字典进行序列化:
       import json
       res = json.dumps(result_dict, ensure_ascii=False)

19. 怎么判断一个列表为空?
     根据长度来进行判断

20.  章节目录结构?
{
    "code": 200,
    "message": "OK",
    "data": [
        {
            "id": 1,
            "description": null,
            "enabled": true,
            "create_datetime": "2020-08-20T11:45:54Z",
            "update_datetime": "2020-08-20T11:45:56Z",
            "delete_datetime": null,
            "name": "第一章 初级会计入门",
            "num_id": 1,
            "parent_id": null,
            "resource_id": "meiya_niubi",
            "path": null,
            "audition": false,
            "data": [
                {
                    "id": 3,
                    "parent_id": 1,
                    "name": "第一章 第一讲",
                    "num_id": 1,
                    "resource_id": "meiya_niubi",
                    "path": "//dic1",
                    "audition": 0
                },
                {
                    "id": 4,
                    "parent_id": 1,
                    "name": "第一章 第二讲",
                    "num_id": 2,
                    "resource_id": "meiya_niubi",
                    "path": "//dic2",
                    "audition": 0
                }
            ]
        },
        {
            "id": 2,
            "description": null,
            "enabled": true,
            "create_datetime": "2020-08-20T11:45:54Z",
            "update_datetime": "2020-08-20T11:45:56Z",
            "delete_datetime": null,
            "name": "第二章 初级会计入门",
            "num_id": 2,
            "parent_id": null,
            "resource_id": "meiya_niubi",
            "path": null,
            "audition": false,
            "data": [
                {
                    "id": 5,
                    "parent_id": 2,
                    "name": "第二章 第一节",
                    "num_id": 1,
                    "resource_id": "meiya_niubi",
                    "path": null,
                    "audition": 0,
                    "data": [
                        {
                            "id": 7,
                            "parent_id": 5,
                            "name": "第二章 第一节 第一讲",
                            "num_id": 1,
                            "resource_id": "meiya_niubi",
                            "path": "//dic3",
                            "audition": 0
                        }
                    ]
                },
                {
                    "id": 6,
                    "parent_id": 2,
                    "name": "第二章 第二节",
                    "num_id": 2,
                    "resource_id": "meiya_niubi",
                    "path": null,
                    "audition": 0,
                    "data": [
                        {
                            "id": 8,
                            "parent_id": 6,
                            "name": "第二章 第二节 第一讲",
                            "num_id": 1,
                            "resource_id": "meiya_niubi",
                            "path": "//dic4",
                            "audition": 0
                        },
                        {
                            "id": 9,
                            "parent_id": 6,
                            "name": "第二章 第二节 第二讲",
                            "num_id": 1,
                            "resource_id": "meiya_niubi",
                            "path": "//dic5",
                            "audition": 0
                        }
                    ]
                }
            ]
        }
    ],
    "elapsed": 70
}

21. 怎么序列化日期字段,类型为DateTimeField?
     对日期进行转字符串，然后对记录进行单独的Json.dumps
     
     
22. 
     
23. 序列化的时候怎么要选择数据库？
    如果你选择另外一个admin库查询，但是作序列化时会自动关联到该应用默认的数据库，做序列化时会默认选择default数据库。
  
  解决返回中文乱码的问题:
  def test(request):
    result = {"status":"错误","data":"","city":"北京"}
    #json返回为中文
    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    
    
 24. querySet是不能直接序列化的。
      特別是Filter后，需要用First()或者for循环遍历获取内容，然后再序列化，才能获取到指定的值。
    
      
    
  
 25. 怎么对timezone下的2020-08-28 08:42:35.455495+00:00进行转化为对应的日期类型
      直接转换为字符串类型的日期，然后截取日期即可。
      
 26.  2020-08-28 16:56:01,807 WARNING  csrf.py:149 : Forbidden (CSRF cookie not set.): /app/pay
      可以使用@csrf_exempt注解来忽略django的csrf认证。
 
 
 27.  对接支付宝支付。
 
 28. choices的使用。
      可以通过给models的Integer字段选为choices，然后根据chioces获取到对应的中文返回。
 
29. 怎么批量创建对象? 
     根据objects.bulk_create()方法来创建，批量创建的对象会直接插入到数据库中
 b = User(username=uid)
        q = []
        for i in range(0, 10):
            q.append(b)
        users = User.objects.bulk_create(q)

30. 怎么查看models执行的sql日志?
    from django.db import connection
    print(connection.queries)
    

31. filter怎么判断不等于?
    from django.db.models import Q
     ~Q(username="zhangsan")
     
32. eval()函数，不能处理null，需要将null转换为None才行，否则会报错undefine


33. 分组查询，需要配合.annote()一起使用。in_student为别名
    schs = Schedule.objects.filter(student=s).values("resource_id").annotate(in_student=Min("id"))
            print(schs.query)


34. 使用URLField能将url的地址的内容展示出来
   URLField


35. 在设置model时，可以设置null或者空。
     null=True, blank=True