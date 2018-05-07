#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

class IPClass:
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    def get_ip(self):
        return self.ip
    def set_ip(self,ip):
        self.ip=ip

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def __str__(self):
        print("ip:",self.ip,"port:",self.port)


