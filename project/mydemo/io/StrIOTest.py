#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
from io import StringIO,BytesIO

f=StringIO("hello\nhi\nGoodbye")
count=0
while True:
    s=f.readline()
    if s =="" or s==" ":
        break
    print(s)
    count += 1
print(count)

b=BytesIO()
b.write("存入".encode("utf-8"))
print(b.getvalue())

br=BytesIO(b'\xe5\xad\x98\xe5\x85\xa5')
print(br.readline())



