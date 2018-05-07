#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
#Python对SMTP支持有smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮
from email import mime, encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
__author__ = 'xiaox'

#创建纯文本的邮件对象
#msg=MIMEText("hello python ! \n hello mail !" ,"plain","utf-8" )
#msg = MIMEText('<html><body><h1>Hello</h1>' +
#    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#    '</body></html>', 'html', 'utf-8')

msg=MIMEMultipart("alternative")#alternative表示发送html时候附加text格式,如果读取不到html回自动降级为纯文本(text)
#添加邮件正文
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '<p><img src="cid:1"></p>' +
    '</body></html>', 'html', 'utf-8'))
msg.attach(MIMEText('hello', 'plain', 'utf-8'))

count=0
for x in ["avatar.jpg","yinhun.jpg"]:
    with open(x,"rb") as f :
        # # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase("image", "jpg", filename=x)
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename=x)
        mime.add_header('Content-ID', '<%s>'% count)#定义图片 ID，在 HTML 文本中引用
        mime.add_header('X-Attachment-Id', '%s'% count)
        # 读取图片信息
        mime.set_payload(f.read())
        # 编码
        encoders.encode_base64(mime)
        msg.attach(mime)
        count+=1



from_addr = "xiaoxiang0719@126.com"
password="xx19931026"

#收件人地址
to_addr="313721087@qq.com"

#stmp服务器地址
stmp_server="smtp.126.com"

#发送邮箱地址
msg['From'] = from_addr
#收件箱地址
msg['To'] = to_addr
#主题
msg['Subject'] = 'Python SMTP 邮件测试'

import smtplib
server=smtplib.SMTP(stmp_server,25)#smtp协议默认端口为25
server.set_debuglevel(1)#就可以打印出和SMTP服务器交互的所有信息
server.login(from_addr,password)#登录SMTP服务器
server.sendmail(from_addr,[to_addr],msg.as_string())#发邮件，由于可以一次发给多个人，所以传入一个list
