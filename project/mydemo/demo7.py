#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print("hello word")
    elif len(args)==2:
        print("hello %s" %args[1])
    else:
        print('Too many arguments!')
print(__name__)
print(sys.argv)
if __name__=='__main__':
    test()
