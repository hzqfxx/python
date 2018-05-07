#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
class Student(object):

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s=Student()
s.score=100
print(s.score)


#请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if isinstance(value,(int,float)):
            self._width=value
        else:
            raise TypeError("参数错误!")

    @property
    def height(self):
        return self._height

    @width.setter
    def height(self, value):
        if isinstance(value, (int, float)):
            self._height = value
        else:
            raise TypeError("参数错误!")

    @property
    def resolution(self):
        return self._height*self._width

s1 = Screen()
s1.width = 1024
s1.height = 768
print('resolution =', s1.resolution)
if s1.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')