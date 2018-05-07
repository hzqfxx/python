#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

import mysql.connector
conn=mysql.connector.connect(user="root",password="123",database='test')
cursor = conn.cursor()
#创建表
#cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#插入一行记录
cursor.execute('insert into user (id, name) values (%s, %s)', ['4', 'Michael'])
cursor.rowcount


#查询
cursor=conn.cursor()
cursor.execute("select * from USER ")
values=cursor.fetchall()
print(values)
#提交事务
conn.commit()
cursor.close()
conn.close()