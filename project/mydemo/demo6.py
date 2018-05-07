#!C:/Users/xiaox/Anaconda3 python
# -*-coding：utf-8 -*-

import functools
import datetime
import time

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print("好像代理啊! 执行%s 方法%s()" %(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

@log("execute")
def date():
    print("2018-4-20")
date()
print(date.__name__)

def log2(func):
    @functools.wraps(func)
    def wrapper2(*args,**kw):
        print("call %s()" %(func.__name__))
        return func(*args,**kw)
    return wrapper2
@log2
def date2():
    print("2018-4-21")
date2()
print(date2.__name__)
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
def metric(fn):
    @functools.wraps(fn)
    def dates(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        return fn(*args,**kw)
    return dates

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
#将字符串转为2进制
print( int("10010010",base=2))

def int2(n,base=2):
    return int(n,base)

print(int2("0101000111010"))

int8=functools.partial(int,base=8)
print(int8("10"))





