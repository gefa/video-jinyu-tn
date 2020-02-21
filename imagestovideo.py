#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 18:03:47 2020

@author: taimaame
"""

import os
import cv2
import wordtoimage2



def imagetovideo(username,keyword):
    file_dir=wordtoimage2.draw_test(username,keyword)
    list=[]
    for root,dirs,files in os.walk(file_dir):
        for file in files:
           list.append(file)  #获取目录下文件名列表
    video=cv2.VideoWriter('../'+username+'/'+username+'.avi',cv2.VideoWriter_fourcc(*'MJPG'),0.5,(1280,720))  #定义保存视频目录名称及压缩格式，fps=10,像素为1280*720
    for i in range(1,len(list)+1):
        img=cv2.imread(file_dir+list[i-1])  #读取图片
        img=cv2.resize(img,(1280,720)) #将图片转换为1280*720
        video.write(img)   #写入视频
    video.release()
 
if __name__ == '__main__':
   
    username = input('Enter your username: ')
    keyword = input('Enter the keyword you would like to search: ')
    imagetovideo(username,keyword)