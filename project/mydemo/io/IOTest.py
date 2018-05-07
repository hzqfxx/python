#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

from collections import Iterable
#读取文件,释放资源
f = open('F:/test.txt',"r")
#try方式读取文件,释放资源
try:
    print(f.read())
finally:
    if f:
        f.close()

#with方式读取文件,释放资源
with open('F:/test.txt',"r") as x:
    print(isinstance(x ,Iterable))
    for n in x:
        print(n,"一行")


with open('F:/394877.jpg',"rb")as j:
    print(j.read())

with open('F:/test.txt',"r",encoding="shift-jis",errors='ignore') as x:
    print(x.read())

with open('F:/test.txt',"a") as w:
    w.write("add2")
