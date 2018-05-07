#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

#导入模块
from project.mydemo.test2 import PrivateTest
def test(name):
    return PrivateTest.getting(name)
print(test(1))