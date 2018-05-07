#!C:/Users/xiaox/Anaconda3 python
# -*-coding：utf-8 -*-
import os # 导入os模块
print(list(range(1,11)))

list=[]
for x in range(1,11):
    list.append(x*x)
print(list)

print([x*x for x in  range(1,11) if x%2==0])

print([x+y for x in "abc" for y in "EFG"])

print([d for d in os.listdir(".")])

L = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L if isinstance(x,str)]
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')


