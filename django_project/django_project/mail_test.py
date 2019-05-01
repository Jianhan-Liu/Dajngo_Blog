"""
  Created by PyCharm.
  User: Liujianhan
  Date: 2019/5/1
  Time: 0:10
 """
__author__ = 'liujianhan'

import os

from django.core.mail import send_mail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

send_mail(
    '邮件主题',
    '邮件内容',
    'lorgerd@163.com',  # 发件人
    ['790069398@qq.com', 'lorgerd@163.com', 'jianhan.liu@aliyun.com', 'liujianhan@gmail.com'],  # 收件人，必须是列表类型
    fail_silently=False,
)
print('Done!')
