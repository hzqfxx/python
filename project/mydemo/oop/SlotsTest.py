#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

from types import MethodType
class Student(object):
    #使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
    #__slots__ = ("name","age","set_sum","num")
    pass

s=Student()
s.name="张三"
print(s.name)

#绑定方法
def set_sum(self,num):
    self.num = num+1

s.set_sum=MethodType(set_sum,s)
s.set_sum(230)
print(s.num)

def age(self,age):
    self.age=age
    print("s绑定所有实例")

Student.age=age
s2=Student()
s.age(123)
s2.age(234)
print(s.age)
print(s2.age)
print(Student.__name__)


class test(object):
    __slots__ = ('a', 'b')
    c = 5

    def init(self):
        pass

t=test()
t.a=3
t.b=4
test.a=5
print(t.a)
t.a =3