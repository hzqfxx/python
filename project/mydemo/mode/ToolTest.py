#!C:/Users/xiaox/Anaconda3 python
# -*- coding: utf-8 -*-
' what？ '
__author__ = 'xiaox'
import os
from PIL import Image, ImageFilter

im=Image.open("image.jpg")
#获取图片尺寸
w,h=im.size
print("image size :  %s,%s"% (w,h) )

#缩放
im.thumbnail((w/2,h/2))
print("缩放后高宽 %s,%s" % (w/2,h/2))
im.save("image2.jpg","jpeg")

# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')





