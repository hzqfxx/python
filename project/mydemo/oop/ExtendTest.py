#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

class Person:
    def hobbies(self):
        print("person is obj")

class ZhangSan(Person):
    def hobbies(self):
        print("ZhangSan  hobbies  eat")

class LiSi(Person):
    def hobbies(self):
        print("LiSi  hobbies  book")

class Customer:
    def hobbies(self):
        print("Customer  hobbies  Calculate")

def say (student):
    student.hobbies()
p1=Person()
p2=ZhangSan()
p3=LiSi()
p4=Customer()

say(p1)
say(p2)
say(p3)
say(p4)








