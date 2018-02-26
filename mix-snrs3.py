# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 14:29:10 2018

@author: onion
"""
#针对按信噪比分别存放图片的多个训练文件夹（例如20个文件夹）。将20个信噪比的图片，按照输入的信噪比范围揉和成训练集
import os
import shutil


# 新建文件夹

path1 ='./trainpics/'
mixsnrsfiles=os.listdir(path1)
#files=[SNR0,SNR10,SNR12,SNR14,SNR16,SNR18,]

#规定所需要的SNR的范围 [a,b]
a=2
b=2
SNR_range=[x for x in range(a, b+2, 2)]
name1=str(a)
name2=str(b)
picspath=path1+'snr'+name1+'to'+name2

#%% 新建文件夹
if picspath not in mixsnrsfiles:
    os.mkdir(picspath)
   
path2='./pics-every_snrs'
evrsnrsfiles=os.listdir(path2)   
    
#%%
for evrSNR in SNR_range:
    if evrSNR < 0:
        SNRlabel = abs(evrSNR)
        for evrfile in evrsnrsfiles[10:]:
            if SNRlabel == int(evrfile[4:]):
                pathevr = path2+'/'+ evrfile
                pics=os.listdir(pathevr)
                for evr in pics:
                    newpath = picspath+'/'+ evr
                    oldpath = pathevr + '/'+ evr
                    shutil.copy(oldpath,newpath)
            else:
                continue
                
    elif evrSNR >= 0:
        SNRlabel=evrSNR
        for evrfile in evrsnrsfiles[:10]:
            if SNRlabel == int(evrfile[3:]):
                pathevr = path2+'/'+ evrfile
                pics=os.listdir(pathevr)
                for evr in pics:
                    newpath = picspath+'/'+ evr
                    oldpath = pathevr + '/'+ evr
                    shutil.copy(oldpath,newpath)  
            else:
                continue                           
     
 #%%   
      
                      
        
                
                
        
    
    