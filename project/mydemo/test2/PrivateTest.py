#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

def _private_1(name):
    return 'Hello ! %s' % name

def _private_2(name):
    return 'Hi ! %s' % name

def getting(name):
    if name < 3:
        return _private_1(name)
    else:
        return _private_2(name)

