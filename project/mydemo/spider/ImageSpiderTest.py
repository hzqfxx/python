#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
import json

__author__ = 'xiaox'
import requests

if __name__ == '__main__':
     target = 'http://unsplash.com/napi/feeds/home'
     target1='https://api.unsplash.com/feeds/home?after=84abe580-49e0-11e8-8080-800077d69f79'
     #设置vertify为False绕过SSL认证
     headers={"authorization":"Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09"}
    # req = requests.get(url=target1,headers=headers,verify=False)
    #print(req.text)
     #转为json获取数据
     #html=json.loads(req.text)
     #获取下一页地址
     #next_page=html["next_page"]
     #next_page=target+next_page.split("?")[1]
     #print("下一页地",next_page)
     #下载地址为
     #download="https://unsplash.com/photos/xxxx/download?force=true"
     #for images_url in  html["photos"]:
     #   print("图片地址：",images_url["id"])
photos_id=[]
target = 'http://unsplash.com/napi/feeds/home'
headers = {"authorization": "Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09"}
#req = requests.get(url=target, headers=headers, verify=False)
#print(req.text)
def get_ids():
    req = requests.get(url=target, headers=headers, verify=False)
    html = json.loads(req.text)
    next_page = "http://unsplash.com/napi/feeds/home?" + html["next_page"].split("?")[1]
    for each in html['photos']:
        photos_id.append(each['id'])
    #time.sleep(1)
    for i in range(5):
        req = requests.get(url=next_page, headers=headers, verify=False)
        html = json.loads(req.text)
        next_page = "http://unsplash.com/napi/feeds/home?" + html["next_page"].split("?")[1]
        for each in html['photos']:
            photos_id.append(each['id'])
        #time.sleep(1)
get_ids()
print(photos_id)
