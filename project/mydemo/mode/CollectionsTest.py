#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
from datetime import datetime
import time

#namedtuple是一个函数，它用来创建一个自定义的tuple对象
Point=namedtuple("p",["x","y"])
p=Point(1,2)
print(p.x,p.y)
print(isinstance(p,tuple))
print(isinstance(p,Point))

#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
list1=[]
list2=deque([])
start2=datetime.now().timestamp()
for x in range(100000):
    list2.append(x)
end2=datetime.now().timestamp()
print("deque 所用时间:",(end2-start2))

start=datetime.now().timestamp()
for x in range(100000):
    list1.append(x)
end=datetime.now().timestamp()
print("list 所用时间:",(end-start))

#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
dd=defaultdict(lambda :"默认值value")
dd["key1"]=123
print(dd["key1"])
print(dd["key2"])

#OrderedDict的key是有序的--注:OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
dd={"a":1,"b":2,"c":3}
print(dd)
dd2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(dd2)
od=OrderedDict()
od["z"]=1
od["y"]=2
od["x"]=3
print(od.keys())

#Counter是一个简单的计数器，例如，统计字符出现的个数：
c=Counter()
for x in  "sdfghiuwhfwhevsdnv":
    c[x]=c[x]+1
print(c)






