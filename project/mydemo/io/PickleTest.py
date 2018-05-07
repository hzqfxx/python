#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
#序列化
import pickle
d = dict(name="Bob",age=20)
print(pickle.dumps(d))

f=open("test.txt","wb")
pickle.dump(d,f)
f.close()

f2=open("test.txt","rb")
d2=pickle.load(f2)
f.close()
print(d2)

#序列化为json
import json
d3=dict(name="zhangsan",age=10)
print(json.dumps(d3))

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class Student(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def __str__(self):
        return "name:%s age:%s" %(self._name,self._age)

s=Student("lisi",10)
j2=json.dumps(s,default=lambda obj:obj.__dict__)
print("json,",j2)

def jsonToObj(b):
    return Student(b["_name"],b["_age"])

print(json.loads(j2,object_hook=jsonToObj))

print("==================")

obj = dict(name='小明', age=20)
s5 = json.dumps(obj, ensure_ascii=True)
s6 = json.dumps(obj, ensure_ascii=False)
print(s5)
print(s6)

