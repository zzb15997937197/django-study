from rest_framework import serializers

from polls.models import User, MyClassReource, ScheduleDirecotryResource


class UserSerializers(serializers.ModelSerializer):
    gender_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "password", "gender", "gender_name"]

    @staticmethod
    def get_gender_name(obj):
        gender = obj.gender
        if gender == 0:
            return "男"
        else:
            return "女"


class MyClassInfoSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='student.id')
    user_name = serializers.CharField(source='student.name', allow_blank=True, allow_null=True)
    resource_package_id = serializers.CharField(source='rource.id', allow_blank=True, allow_null=True)
    resource_name = serializers.CharField(source='rource.name', allow_blank=True, allow_null=True)
    resource_price = serializers.CharField(source='rource.price', allow_blank=True, allow_null=True)
    resource_sales = serializers.CharField(source='rource.sales', allow_blank=True, allow_null=True)
    resource_description = serializers.CharField(source='rource.description', allow_blank=True,
                                                 allow_null=True)

    class Meta:
        model = MyClassReource
        fields = ('user_id',
                  'user_name',
                  'resource_package_id',
                  'resource_name',
                  'resource_price',
                  'resource_sales',
                  'resource_description')


class ScheduleDirectorySerializers(serializers.ModelSerializer):
    # id,create_datetime,parent_id,name,resource_id,path,audition
    class Meta:
        model = ScheduleDirecotryResource
        fields = ("id", "create_datetime", "parent_id", "name", "resource_id", "path", "audition")
