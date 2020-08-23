from polls.BaseView import BaseView
from django.utils import timezone
from polls.HttpResult import Result
from polls.models import ScheduleDirecotryResource
from polls.Serializers import ScheduleDirectorySerializers
import json


class Test01(BaseView):

    def get(self, request, format=None):
        r = Result()

        now = timezone.now().time()
        print(now)
        return self.s_result(r)


# 获取章节目录(ScheduleDirecotryResource)
class Test02(BaseView):
    sql = "select id,create_datetime,parent_id,name,resource_id,path,audition from schedule_directory_resource where parent_id =%s"

    def get(self, request, uid):
        r = Result()
        alls = ScheduleDirecotryResource.objects.all().filter(resource_id=uid, parent_id=None)
        try:
            if len(alls) > 0:
                self.datas = []
                for i in alls:
                    # 根据父亲去找儿子
                    # 遍历子目录，然后将子记录序列化后添加到父记录里。
                    datas = []
                    results = self.rawSQL(self.sql, [i.id])
                    d = ScheduleDirectorySerializers(i).data
                    for j in results:
                        datas.append(ScheduleDirectorySerializers(j).data)
                    d["data"] = datas
                    self.datas.append(d)
                    self.set_child(self, datas)
                r.data = self.datas
            else:
                raise Exception("没有找到课程" + uid + "!")
        except Exception as e:
            r.error(e)
        return self.s_result(r)

    @staticmethod
    def set_child(self, results):
        # 根据当前id作为parent_id去查询其他记录
        for i in results:
            id = i["id"]
            res_datas = []
            res = self.rawSQL(self.sql, [id])
            if res is None or len(res) == 0:
                continue
            else:
                for m in res:
                    res_datas.append(ScheduleDirectorySerializers(m).data)
                print("二级目录:", self.datas)
                for j in self.datas:
                    s_data = j["data"]
                    for k in s_data:
                        if k["id"] == id:
                            datas = []
                            for q in res_datas:
                                datas.append(ScheduleDirectorySerializers(q).data)
                            k["data"] = datas
                    print(id, "找到孩子:", res)
            self.set_child(self, datas)
    # 表示id不为任何记录的父母id,那么为叶子节点，叶子节点可能在第二层或者是第三层。
