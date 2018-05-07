#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
import socket,threading
import time
#服务端
#创建socket对象
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",9998))
#监听端口
s.listen(5)
print('Waiting for connection...')

def infoHandler(sock,addr):
    print("接收到请求")
    #发送数据
    sock.send(b'Welcome!')
    #处理数据
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        #if not data or data.decode("utf-8")=="exit":
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

#处理接收到的请求
while True:
    sock,addr=s.accept()

    t=threading.Thread(target=infoHandler,args=(sock,addr))
    t.start()





