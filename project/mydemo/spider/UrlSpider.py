#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
import requests
if __name__ == '__main__':
    target = 'http://gitbook.cn/'
    req = requests.get(url=target)
    print(req.text)

