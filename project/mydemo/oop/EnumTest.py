#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

from enum import Enum,unique
from collections import Iterable

Month=Enum("Month",('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
print(Weekday.Fri)
print(Weekday.Sat)
print(Weekday.Mon.value)

print(isinstance(Weekday.__members__.items(),Iterable))

for name,member in Weekday.__members__.items():
    print(name, '=>', member, ',', member.value)

#把Student的gender属性改造为枚举类型，可以避免使用字符串
@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        if isinstance(gender,str):
            raise TypeError("参数类型错误")
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


