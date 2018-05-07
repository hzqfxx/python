#!C:/Users/xiaox/Anaconda3 python
#-*-coding：utf-8 -*-

#filter
from collections import Iterable
def is_odd(n):
    return n%2==1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A', '', 'B','C', None,  '  '])))

print(sorted([2,5,7,-10,-6,-3,8,4],key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True))

#排序

#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[-1]
print(sorted(L,key=by_name))
print(sorted(L,key=by_score,reverse=True))

#返回函数,不是调用函数
def lazy_sum(*num):
    def calc_sum():
        ax = 0
        for n in num:
            ax += n
        return ax
    return calc_sum
sum1=lazy_sum(1,2,3,4,5)
print(sum1())

#每次调用返回的都是已个新的函数
sum2=lazy_sum(1,2,3,4,5)
sum3=lazy_sum(1,2,3,4,5)
print(sum2==sum)

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1 = count()
for x1 in f1:
    print(x1())

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

#使用匿名函数改造
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print(list(filter(lambda x:x%2==1,range(1,20))))




