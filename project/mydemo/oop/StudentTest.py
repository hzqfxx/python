#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

class Student(object):
    #属性加上__表示private
    def __init__(self,name,age):
        self.__name=name
        self.age=age

    def print2(self):
        print("name=",self.__name,"age=",self.age)

    def get_name(self):
        return self.__name

    def set_name(self, names):
        self.__name = names
s1=Student("张三",18)
#实例可以添加属性,所以一个类的不同对象可以拥有不同的属性
s1.set_name("123")
s1.get_name()
print(s1.get_name())

#请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    def __init__(self, name, gender):
        if isinstance(name,str) and isinstance(gender,str):
            self.name = name
            self.__gender = gender
        else:
            raise TypeError("参数类型错误")

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender

bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

