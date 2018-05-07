#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

import os,time

print(os.name)

print(os.environ)

print(os.environ.get('PATH'))
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join("C:\\Users\\xiaox\\PycharmProjects\\untitled\\project\\mydemo\\io","testdir"))
#添加文件
#print(os.mkdir("C:\\Users\\xiaox\\PycharmProjects\\untitled\\project\\mydemo\\io\\testdir"))
#删除文件
#print(os.rmdir("C:\\Users\\xiaox\\PycharmProjects\\untitled\\project\\mydemo\\io\\testdir"))
# 时间戳格式转换
def timenum2str(timenum):
    # print('timenum = ', timenum)
    t = time.localtime(timenum)
    # print('t = ', t)
    return time.strftime('%Y-%m-%d %H:%M', t)

# 获取文件的修改时间
def getTime(filepath):
    t = os.path.getmtime(filepath)
    return timenum2str(t)

# 获取文件大小（单位：字节）
def getSize(filepath):
    s = str(os.path.getsize(filepath))
    while True:
        if len(s) < 5:
            s = ' ' + s
        else:
            break
    return s

if __name__ == '__main__':
    for f in [x for x in os.listdir('.')]:
        print(getSize(f), getTime(f), ' ', f)

#查询该目录下指定文件(包括子目录)

def find_file(path,fileName):
    for dir_name in os.listdir(path):
        #文件
        if os.path.isfile(dir_name):
            if fileName in dir_name:
                print(os.path.join(os.getcwd()),dir_name)
        #文件夹
        if os.path.isdir(dir_name):
            os.chdir(dir_name)
            find_file(".",fileName)
    os.chdir("..")
find_file(".","a")



def find_file(path, name):
    for dir_name in os.listdir(path):
        if os.path.isfile(dir_name):
            if name in dir_name:
                print(os.getcwd())
                print(os.path.join(os.getcwd(), dir_name))
        elif os.path.isdir(dir_name):
            os.chdir(dir_name)
            find_file('.', name)
    os.chdir('..')

find_file('.', 'a')
print("==========================================")
print(os.listdir("."))
