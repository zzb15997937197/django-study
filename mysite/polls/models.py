from django.db import models
import Constant
import hashlib
from django.utils import timezone
from django.db.models.query import QuerySet


class TimestampQuerySet(QuerySet):
    def delete(self):
        self.update(delete_datetime=timezone.now())


class TimestampManager(models.Manager):
    _queryset_class = TimestampQuerySet

    def get_queryset(self):
        kwargs = {'model': self.model, 'using': self._db}
        if hasattr(self, '_hints'):
            kwargs['hints'] = self._hints
        return self._queryset_class(**kwargs).filter(delete_datetime__isnull=True)


# 以下的UserTest会生成一个myapp_usertest表，在Meta类里添加表的信息。
GENDER_CHOICE = (
    (0, '男'),
    (1, '女'),
)


class User(models.Model):
    username = models.CharField(max_length=20, verbose_name="用户名", null=True)
    password = models.CharField(max_length=20, verbose_name="密码", null=True)
    gender = models.IntegerField(verbose_name="性别", choices=GENDER_CHOICE, default=0, null=False)
    age = models.IntegerField(verbose_name="年龄", default=0)

    def __str__(self):
        return "用户测试表"

    def introduce(self):
        return "you username is " + self.username

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = "用户表"
        db_table = "sys_user"


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    # 有一个外键，blog_id，会直接关联到Blog表。
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    ##多对多关联关系，author表与entry表存在多对多的关系,通过entry_id和author_id来关联
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

    # 资源包


GENDER_CHOICE = (
    (0, '男'),
    (1, '女'),
)

EDUCATION_CHOICE = (
    (0, '初中'),
    (1, '高中'),
    (2, '大专'),
    (3, '本科'),
    (4, '硕士'),
    (5, '博士'),
)

GOAL_CHOICE = (
    (0, '一年目标'),
    (1, '3-5 年目标'),
    (2, '长期目标'),
)


class BaseModel(models.Model):
    description = models.CharField(max_length=180, verbose_name='描述', default='', null=True, blank=True)
    enabled = models.BooleanField(verbose_name='有效', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        s = self.name if hasattr(self, 'name') else self.description
        return '' if s is None else s


class TimestampModel(BaseModel):
    create_datetime = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    update_datetime = models.DateTimeField(verbose_name='更新时间', default=timezone.now)
    delete_datetime = models.DateTimeField(verbose_name='删除时间', null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.delete_datetime = timezone.now()
        self.save(using=using)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.update_datetime = timezone.now()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

    class Meta:
        abstract = True

    objects = TimestampManager()


class Student(TimestampModel):
    name = models.CharField(max_length=Constant.db_name_length, verbose_name='学员昵称', null=False)
    phone = models.CharField(max_length=Constant.db_phone_length, unique=True, verbose_name='手机号', null=False)
    password = models.CharField(max_length=Constant.db_password_length, verbose_name='密码')
    avatar = models.CharField(max_length=Constant.db_url_length, verbose_name='头像', null=False)
    real_name = models.CharField(max_length=Constant.db_name_length, verbose_name='真实姓名', null=False)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_CHOICE, default=0, null=False)
    birthday = models.DateField(verbose_name='出生日期')
    education = models.IntegerField(verbose_name='学历', choices=EDUCATION_CHOICE, default=0)
    signature = models.CharField(max_length=Constant.db_description_length, verbose_name='签名')
    learn_target = models.CharField(max_length=Constant.db_description_length, verbose_name='学习目的')
    learn_goal = models.IntegerField(choices=GOAL_CHOICE, verbose_name='学习目标')
    address = models.CharField(max_length=Constant.db_address_length, verbose_name='收货地址')
    amount = models.DecimalField(verbose_name="金额", max_digits=3, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name_plural = '学员'
        verbose_name = '学员'
        db_table = 'student'

    def save(self, *args, **kwargs):
        md5 = hashlib.md5()
        md5.update(self.password.encode())
        self.password = md5.hexdigest()
        super(Student, self).save(*args, **kwargs)


class ResourcePackage(TimestampModel):
    # 资源包 id
    # 资源包名
    name = models.CharField(max_length=200, verbose_name='资源名', null=False)

    # 原始报价
    price = models.FloatField(verbose_name='报价', default=1.0, null=False)
    # 实际售价
    sales = models.FloatField(verbose_name='实际售价', default=1.0, null=False)

    uid = models.CharField(verbose_name='资源包uid', unique=True, max_length=32, null=False)

    class Meta:
        verbose_name_plural = '资源包'
        verbose_name = '资源包'
        db_table = 'resource_package'


# 我的班级，即课程包,学生和资源一对多
class MyClassReource(models.Model):
    student = models.ForeignKey(Student, verbose_name='资源', to_field='id',
                                related_name='student_id',
                                on_delete=models.DO_NOTHING)
    rource = models.ForeignKey(ResourcePackage, to_field='id', related_name="resource_package_id",
                               on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "我的班级表"

    class Meta:
        verbose_name = "我的班级"
        verbose_name_plural = "我的班级资源包"
        db_table = "user_to_resource"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        indexes = [
            # 联合索引，遵循mysql的最左匹配原则
            models.Index(fields=['last_name', 'first_name']),
            # 单个索引
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]
        # 唯一性约束
        unique_together = ('first_name', 'last_name',)
        verbose_name = "客户表"
        verbose_name_plural = "客户表"
        db_table = "sys_customer"


# 反馈类型表
class FeedBackType(TimestampModel):
    name = models.CharField(max_length=50, verbose_name="类型名称")

    class Meta:
        verbose_name_plural = "学生反馈类型表"
        verbose_name = "学生反馈类型表"
        db_table = "student_feedback_type"


# 学生反馈
class Feedback(TimestampModel):
    feedback_content = models.TextField(verbose_name='反馈内容', null=False)
    feedback_class = models.IntegerField(verbose_name='反馈类型')
    student = models.ForeignKey(Student, to_field="id", verbose_name="学生id", null=True, blank=True,
                                on_delete=models.DO_NOTHING)
    type = models.ForeignKey(FeedBackType, to_field="id", verbose_name="类型id", null=True, blank=True,
                             on_delete=models.DO_NOTHING)

    def get_model_fields(self):
        return self._meta.fields

    class Meta:
        verbose_name_plural = "学生反馈表"
        verbose_name = "学生反馈表"
        db_table = "student_feedback"




DIRECTORY_RESOURCE_CHOICES = (
    (1, '理论须知'),
    (2, '音频图文'),
    (3, '练习'),
    (4, '课件'),
)


class ScheduleDirecotryResource(TimestampModel):
    name = models.CharField(max_length=Constant.db_name_length, verbose_name="资源的名称", null=True)
    num_id = models.IntegerField(verbose_name="章节顺序", null=True)
    parent_id = models.IntegerField(verbose_name="父节点Id", null=True)
    resource_id = models.CharField(max_length=Constant.db_name_length, verbose_name="资源id,属于哪个课程下的")
    path = models.CharField(max_length=Constant.db_description_length, verbose_name="资源路径", null=True)
    audition = models.BooleanField(verbose_name="是否可试听", default=False)
    type = models.IntegerField(verbose_name="类型", choices=DIRECTORY_RESOURCE_CHOICES, default=1)

    class Meta:
        verbose_name_plural = "课程资源目录表"
        verbose_name = "课程资源目录表"
        db_table = "schedule_directory_resource"
