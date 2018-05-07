#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

class Student(object):
    def __init__(self,name):
        self._name=name
    def __str__(self):
        return "Student Object name : %s" % self._name

    #当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score') 来尝试获得属性，这样，我们就有机会返回score的值：
    def __getattr__(self, item):
        if item=="age":
            return 20
    #使用是实例调用对象
    def __call__(self, *args, **kwargs):
        print("My name is %s"% self._name)
    __repr__=__str__

print(Student("dod"))
s=Student("zhangsan")
s()
#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
print(callable(s))
print(callable(max))
print(callable("123"))

class Fib(object):

    def __init__(self):
        self._a,self._b=0,1

    def __iter__(self):
        return self

    def __next__(self):
        #计算下一个值
        self._a,self._b=self._b,self._a+self._b
        if self._a>1:
            raise StopIteration
        return self._a

for n in Fib():
    print(n)


#链式编程
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
print(Chain().status.user.timeline.list)



