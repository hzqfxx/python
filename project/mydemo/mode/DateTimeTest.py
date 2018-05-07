#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
from datetime import  datetime,timedelta

#当前时间
now=datetime.now()
print(now)
#指定时间
print(datetime(2018,4,25,12,00,19))
#转为时间戳
print(now.timestamp())
#时间戳转时间
print(datetime.fromtimestamp(now.timestamp()))
#字符串转时间
print(datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S'))
#时间转字符串
print(datetime.strftime(now, '%Y/%m/%d %H:%M:%S'))

#时间加减
print(now+timedelta(hours=4))
print(now+timedelta(days=1))

#当前时区
print(datetime.utcnow())