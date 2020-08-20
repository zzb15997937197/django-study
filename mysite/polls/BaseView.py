import datetime
from abc import abstractmethod
from decimal import Decimal

from django.db import connection
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView


class BaseView(APIView):

    def __init__(self, **kwargs):
        self.student = None
        super().__init__(**kwargs)

    @abstractmethod
    def get(self, request, format=None):
        pass

    @abstractmethod
    def put(self, request, format=None):
        pass

    @abstractmethod
    def post(self, request, format=None):
        pass

    @abstractmethod
    def delete(self, request, format=None):
        pass

    def auth(self, request):
        session = request.session.get('student')
        if session is None:
            raise Exception('未授权的访问')

    @staticmethod
    def s_result(result):
        r = result.to_json_string()
        return JsonResponse(result.__dict__,
                            json_dumps_params={'sort_keys': False, 'indent': 4, 'ensure_ascii': False}, safe=False)

    @staticmethod
    def merge_input_data_2_object(i, o):
        for key in i:
            ov = getattr(o, key)
            if ov is not None:
                setattr(o, key, i.get(key, ov))

    @staticmethod
    def merge_object_2_dict(o, d):
        for key in o.__dict__:
            ov = getattr(o, key)
            if ov is not None:
                d[key] = ov

    def rawSQL(self, sql, args=None):

        cursor = connection.cursor()
        cursor.execute(sql, args)
        rows = cursor.fetchall()

        result = []
        row_cnt = len(rows)
        col_cnt = 0 if cursor.description is None else len(cursor.description)

        if col_cnt == 0:
            result = True

        for i in range(0, row_cnt):
            item = {}
            for col in range(0, col_cnt):
                item[cursor.description[col][0]] = rows[i][col]

                if isinstance(item[cursor.description[col][0]], Decimal):
                    item[cursor.description[col][0]] = int(str(item[cursor.description[col][0]]))

            result.append(item)

        return result

    def get_partner(self, request):
        host = request.get_host()
        partner = host[:str(host).index('.')]
        return partner

    def student_auth(self, request):
        if 'student' not in request.session:
            raise Exception('请先登录！')
        else:
            self.student = request.session['student']
            return self.student

    def delete_student_auth(self, request):
        del request.session['student']


class BasePageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page_index'
