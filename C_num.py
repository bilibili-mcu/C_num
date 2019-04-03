#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:07:50 2019

@author: mculi
"""

from tkinter import *
import random

win=Tk();
num=Tk();
win.title('一键C_num By平家MCU')
num.title('数值输出')

f = open('config.txt')
numb = f.read()
f.close()
numb = numb.split();
list = []
for split in numb:
    list.append(int(split))
    
numo = Label(num,text='null',bg='pink',font=('KaiTi', 72),width=10, height=5)
numo.pack()

while 1:
    def g():
        numo.config(text=random.randint(list[0],list[1]))
        numo.pack()
    def b():
        numo.config(text=random.randint(list[2],list[3]))
        numo.pack()
    def a():
        x=random.randint(1,2)
        if x == 1:
            numo.config(text=random.randint(list[0],list[1]))
        if x == 2:
            numo.config(text=random.randint(list[2],list[3]))
        numo.pack()
    
    boy=Button(win,text='女生',font=('KaiTi',36,'bold'),fg='green',bd=2,width=10,command=g)
    girl=Button(win,text='男生',font=('KaiTi',36,'bold'),fg='green',bd=2,width=10,command=b)
    allp=Button(win,text='全部',font=('KaiTi',36,'bold'),fg='green',bd=2,width=10,command=a)

    boy.pack()
    girl.pack()
    allp.pack()
    num.mainloop()
    win.mainloop()
