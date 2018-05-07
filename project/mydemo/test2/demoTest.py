#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
import requests
#去重判断
abc=['112.95.205.246:9999', '13.2.2.2:506', '113.76.96.55:9797']
print(len(abc))
print(len(list(set(abc))))
for x in abc:
    open("C:\\imgSpider\\"+x+".txt","ab+")

print("收到"+str(1+2))

s =requests.session()
print(s)

abc={}
for x in range(1,2):
    pass

bcd=['112.95.205.246:9999', '13.2.2.2:506', '113.76.96.55:9797']
with open("ip.txt","w") as f:
    for x in bcd:
        f.write(x+"\n")