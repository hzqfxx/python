#!C:/Users/xiaox/Anaconda3 python
#-*-coding：utf-8 -*-
#生成器
from collections import Iterable
from functools import reduce
def fn(x,y):
    return x*10+y

def fn2(s):
    digits={"1":1,"2":2,"3":3,"4":4,"5":6}
    print(digits[s])
    return digits[s]

print(reduce(fn,map(fn2,"135")))
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def strTOint(s):
    def fn(x, y):
        return x * 10 + y

    def fn2(s):
        return DIGITS[s]
    return reduce(fn,map(fn2,s))
print( strTOint("654"))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    if isinstance(name,str):
        return name.lower().title()
    return None
names=['adam', 'LISA', 'barT']
print(list(map(normalize,names)))

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
   return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    dotIndex = s.index(".")
    s = s[:dotIndex]+s[dotIndex+1:]
    return reduce(lambda x,y:x*10+y, map(lambda c : digits[c],s))/10**(len(s) - dotIndex)


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print(123465/10**(6-3))
print(10/10)





