#!C:/Users/xiaox/Anaconda3 python
# *-coding：utf-8 -*-

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(args):
    if args==[]:
        return (None,None)
    Max = args[0]
    Min = args[0]
    for n in args:
        if n>Max:
            Max=n
        if n<Min:
            Min=n
    print(Min,Max)
    return (Min,Max)
# 测试itera
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
