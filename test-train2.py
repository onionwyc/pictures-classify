# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 18:27:43 2018

@author: onion
"""
#从分开信噪比的图片中，按照一定的比例，划分出测试集，分别存为一个文件夹。即得到20个训练文件夹，20个测试文件夹。
import os
import shutil

testnums=0.2 #给定比例
path1 ='../pics-every_snrs/'
mixsnrsfiles=os.listdir(path1)

newpath='../testpics'+str(testnums)
os.mkdir(newpath)
#%%
for snrname in mixsnrsfiles:
    pics=os.listdir(path1+snrname)
    for evrpic in pics:
        countlabel=int(evrpic.split('.')[1])
        if countlabel % (int(1/testnums)) == 0 :
            newpath2 = newpath +'/' + evrpic
            oldpath = path1+snrname +'/'+ evrpic
            shutil.move(oldpath,newpath2)  
#%%