#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'

import requests
from bs4 import BeautifulSoup

#整合代码
class downloader(object):
    def __init__(self):
        self.server='http://www.biqukan.com/'
        self.targer = "http://www.biqukan.com/1_1094/"
        self.name=[]#章节名称
        self.url=[]#章节地址
        self.nums=0#章节数

    #获取下载连接
    def get_downloader_url(self):
        req=requests.get(url=self.targer)
        html=req.text
        div_bf=BeautifulSoup(html)
        div = div_bf.find_all("div", class_="listmain")
        a_bf = BeautifulSoup(str(div[0]))
        a=a_bf.find_all("a")
        self.nums=len(a[15:])
        # 抓取所有连接
        a = a_bf.find_all("a")
        for urladdr in a:
            self.name.append(urladdr.string)
            self.url.append(self.server+urladdr.get("href"))

    #获取章节内容
    def get_contents(self,targer):
        req=requests.get(targer)
        html=req.text
        bf=BeautifulSoup(html)
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    #爬取的文章内容写入文件
    def writer(self,name,path,text):
        writer_flag=True
        with open(path,"a",encoding="utf-8") as f:
            f.write(name+"\n")
            f.writelines(text)
            f.write("\n\n")

import sys
if __name__=="__main__":
    d1=downloader()
    d1.get_downloader_url()
    print("《一念永恒》开始下载：")
    for x in range(d1.nums):
        d1.writer(d1.name[x],"一念永恒.txt",d1.get_contents(d1.url[x]))
        sys.stdout.write("  已下载:%.3f%%" %  float(x/d1.nums) + '\r')
        sys.stdout.flush()
    print("《一念永恒》下载完成")