#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
import types
#判断内置对象

print(type(123))

#使用types模块进行判断
#但是!!!能用isinstans的尽量不用types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x:x+x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(dir(abs))

print(len("abc"))
print("abc".__len__())

class Student(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student.count+=1


c1=Student("张三")
