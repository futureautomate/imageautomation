# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 00:36:18 2019

@author: Tejas
"""



from PIL import Image
import os

for i in os.listdir('F:\Channel\Code\Images'): #listing each item in a folder
    files = os.listdir('F:\Channel\Code\Images/%s'%i)
    for j in files:
        img = Image.open('F:\Channel\Code\Images/%s/%s'%(i,j)) # image extension *.png,*.jpg
        new_width  = 200
        new_height = 300
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save('F:\Channel\Code\Images\%s_%s.png'%(i,j)) # format may what u want ,*.png,*jpg,*.gif
