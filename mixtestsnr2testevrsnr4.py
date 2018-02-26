# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:29:36 2018

@author: onion
"""

import shutil
import os
 
#将分开的20个测试集文件夹揉合为一个文件夹
#%%
snrs=['_'+str(2*x) for x in range(10,0,-1)]
snrs2=[x*2  for x in range(0, 10)];
snrs.extend(snrs2)
path = '../testpics0.2/'
files = os.listdir(path)

#%%
for file in files:
    oldfile=path+file
    snr =snrs[(int(file.split('.')[1])-1)//1000]
    each_path = '../test-evrsnr/'+'SNR'+ str(snr)
    if each_path[15:] not in os.listdir('../test-evrsnr'):
        os.mkdir(each_path)
    shutil.copy(oldfile,each_path+'/'+file) 
    #shutil.copy(oldfile,'./every_snrs'+file)
    
    # %%
  
