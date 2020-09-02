import requests
from django.http import HttpResponse
import json
import random
import datetime

import os
from alipay import AliPay
from rest_framework.views import APIView
from django.conf import settings


class OrderUtils:

    @staticmethod
    def get_order_number():
        now = datetime.datetime.now()
        str_time = now.strftime('%Y%m%d%H%M%S')
        # 在加一个4位的随机数
        rand_str = str(random.randrange(1000, 9999))
        return str_time + rand_str


class RequestAPI(APIView):
    # 以下为GET请求
    def get(self, request):
        url = 'https://www.csdn.net/'
        res = requests.get(url)
        return HttpResponse(res.content)


class AliPayView(APIView):
    # 配置地址
    private_path = os.path.join(settings.BASE_DIR, 'zhifubao/keys/app_private.txt')
    public_path = os.path.join(settings.BASE_DIR, 'zhifubao/keys/alipay_public.txt')
    # 获取公私钥字符串
    app_private_key_string = open(private_path).read()
    alipay_public_key_string = open(public_path).read()

    alipay = AliPay(
        appid="2021000118614885",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
        debug=True,  # 上线则改为False , 沙箱True
    )

    def get(self, request, total_pay):
        order_number = OrderUtils.get_order_number()
        print("订单号为:", order_number)
        order_string = self.alipay.api_alipay_trade_page_pay(
            out_trade_no=order_number,
            total_amount=str(total_pay),
            # subject='支付订单:%s' % order_id,
            subject='支付订单',
            # 回调
            return_url=None,
            # 通知
            notify_url=None,
        )
        # 拼接应答地址
        url = 'https://openapi.alipaydev.com/gateway.do?' + order_string
        res = requests.get(url)
        print("res:", res.content)
        return HttpResponse(res.content, "text/html;charset=gb2312")
