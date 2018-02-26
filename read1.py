# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 21:13:07 2018

@author: onion
"""
#将一个文件夹下的混乱的cucuncut中的图片按照信噪比分开，每个信噪比的图片保存为一个文件夹。
import shutil
import os
 

#%%
snrs=['_'+str(2*x) for x in range(10,0,-1)]
snrs2=[x*2  for x in range(0, 10)];
snrs.extend(snrs2)
path = './cycuncut/'
files = os.listdir(path)

#%%
for file in files:
    oldfile=path+file
    snr =snrs[(int(file.split('.')[1])-1)//1000]
    mod=file.split('.')[0]
    each_path = './'+'SNR'+ str(snr)
    if each_path[2:] not in os.listdir('./'):
        os.mkdir(each_path)
    shutil.copy(oldfile,each_path+'/'+file) 
    #shutil.copy(oldfile,'./every_snrs'+file)
    
    # %%
  
