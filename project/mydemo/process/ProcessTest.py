#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 1:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        #time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThreadA')
t2 = threading.Thread(target=loop, name='LoopThreadB')
t.start()
t2.start()
t.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)

balance = 0
#加锁
lock=threading.Lock()
def change_it(n):
    #先存后取
    global balance
    balance = balance+n
    balance = balance-n
def run_thread(n):
    for i in range(1000000):
        #获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
t1=threading.Thread(target=run_thread,args=(5,))
t2=threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print("结果:",balance)



