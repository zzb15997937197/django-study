from polls.BaseView import BaseView
from django.utils import timezone
from polls.HttpResult import Result
import time


class Test01(BaseView):

    def get(self, request, format=None):
        r = Result()

        now = timezone.now().time()
        print(now)
        return self.s_result(r)
