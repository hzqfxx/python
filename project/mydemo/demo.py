#!C:/Users/xiaox/Anaconda3 python
# -*-coding：utf-8 -*
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

#ax2 + bx + c = 0
import math

def quadratic(a,b,c):
    if not (isinstance(a,(int,float)) and isinstance(b,(int,float))  and isinstance(c,(int,float))):
        raise TypeError("参数错误")
    temp=b*b-4*a*c
    if temp<0:
        return "无解"
    elif temp==0:
        return -b/(2*a)
    else:
        return (-b+math.sqrt(temp))/(2*a),(-b-math.sqrt(temp))/(2*a)

print(quadratic(1,3,-4))




