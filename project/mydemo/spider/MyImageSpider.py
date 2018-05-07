#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
import json
from contextlib import closing

__author__ = 'xiaox'
import requests

class get_photos(object):
    def __init__(self):
        self.photos_id=[] #图片id
        self.download_server= "https://unsplash.com/photos/xxx/download?force=true"#图片下载地址
        self.target = 'http://unsplash.com/napi/feeds/home'#抓取地址
        self.headers={"authorization":"Client-ID 72664f05b2aee9ed032f9f4084f0ab55aafe02704f8b7f8ef9e28acbec372d09"}#认证信息

    def get_photos_id(self):
        return self.photos_id

    #获取指定页数的图片url
    def get_ids(self,num):
        for x  in range(num):
            req= requests.get(url=self.target,headers=self.headers,verify=False)
            html = json.loads(req.text)
            # 下一页地址
            self.target = "http://unsplash.com/napi/feeds/home?"+ html["next_page"].split("?")[1]
            for id in html["photos"]:
                self.photos_id.append(id["id"])

    #下载图片
    def download(self, photo_id, filename):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'}
        target=self.download_server.replace("xxx",photo_id)
        with closing(requests.get(url=target,headers=headers,verify=False)) as r:
            with open("C:\\imgSpider\\"+filename+".jpg","ab+") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()
if __name__ == '__main__':
    gp = get_photos()
    print('获取图片连接中:')
    gp.get_ids(5)
    print('图片下载中:')
    for i in range(len(gp.photos_id)):
        print('  正在下载第%d张图片' % (i+1))
        gp.download(gp.photos_id[i],"壁纸"+str(i+1))


