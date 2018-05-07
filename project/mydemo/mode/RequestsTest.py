#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
import requests
#r=requests.get("https://www.douban.com/")
#print(r.status_code)
#print(r.text)

r2 = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
#获取状态码
print(r2.status_code)
#获取实际访问地址
print(r2.url)
#检测编码
print(r2.encoding)
print(r2.content)

r = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
#获取json
print(r.json())
#传入header(dict):
r3 = requests.get('https://www.douban.com/',
                  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r3.text)
#post + data请求:
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})