# import os
# from alipay import AliPay
# from django.conf import settings
#
# # 进行alipay初始化
#
# # 配置地址
# private_path = os.path.join(settings.BASE_DIR, 'apps/order/app_private_key.pem')
# public_path = os.path.join(settings.BASE_DIR, 'apps/order/alipay_public_key.pem')
# # 获取公私钥字符串
# app_private_key_string = open(private_path).read()
# alipay_public_key_string = open(public_path).read()
#
# alipay = AliPay(
#     appid="2016101100664228",
#     app_notify_url=None,  # 默认回调url
#     app_private_key_string=app_private_key_string,
#     alipay_public_key_string=alipay_public_key_string,
#     sign_type="RSA2",
#     debug=True,  # 上线则改为False , 沙箱True
# )
#
#
# def getOrder(order_id, total_pay):
#     order_string = alipay.api_alipay_trade_page_pay(
#         out_trade_no=order_id,
#         total_amount=str(total_pay),
#         subject='支付订单:%s' % order_id,
#         return_url=None,
#         notify_url=None,
#     )
#     # 拼接应答地址
#     return 'https://openapi.alipaydev.com/gateway.do?' + order_string
