# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:17:35 2021
@author: Admin
"""

from math import*
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib as mpl

#Parameters for the forest
a=400  #image height in nb of pixels
b=400  #image width in nb of pixels
density=0.65  #density of the forest
i=random.randint(100, 300) #a random start x point of the fire in center
j=random.randint(100, 300) #a random start y point of the fire in center
p=0.5   #percolation
v=100
w=100

def Create_forest(n,p,d):  
    D=[]
    k=0
    while k<1000:
        if k<d*1000:
            D.append(1)
            k+=1
        else:
            D.append(0)
            k+=1
        
    forest=np.zeros((n,p))
    for y in range(n):
        for x in range(p):
            forest[y,x]=D[random.randint(0,999)]
    return forest
    
    
forest=Create_forest(a,b,density)

forest[i,j]=3

fig = plt.figure(figsize=(15,15))


def step(): 
    Fire=[]  #list containing all the coordinates of burning trees 
    for y in range(a):
        for z in range(b):
            if forest[y][z]==3:
                Fire.append([y,z])
    Perc=[]
    l=0
    while l<1000:
        if l<p*1000:
            Perc.append(3)
            l+=1
        else:
            Perc.append(1)
            l+=1
    for x in range(len(Fire)):
        r=Fire[x][0]
        s=Fire[x][1]

        if forest[r+1,s]==1:
            forest[r+1,s]=Perc[random.randint(0,999)]
        if forest[r+1,s-1]==1:
            forest[r+1,s-1]=Perc[random.randint(0,999)]
        if forest[r+1,s+1]==1:
            forest[r+1,s+1]=Perc[random.randint(0,999)]

        if forest[r-1,s-1]==1:
            forest[r-1,s-1]=Perc[random.randint(0,999)]
        if forest[r-1,s]==1:
            forest[r-1,s]=Perc[random.randint(0,999)]
        if forest[r-1,s-1]==1:
            forest[r-1,s-1]=Perc[random.randint(0,999)]

        if forest[r,s+1]==1:
            forest[r,s+1]=Perc[random.randint(0,999)]
        if forest[r,s-1]==1:
            forest[r,s-1]=Perc[random.randint(0,999)]

    #reducing the trees burnt in the previous step        
    for y in range(len(Fire)):
        forest[Fire[y][0]][Fire[y][1]]=2 
    return forest
        
CM = mpl.colors.ListedColormap([[0.29,0.01,0,0.6],[0.156,0.59,0,1],[0.1,0.1,0.1,1], [0.87,0.3,0.2,0.9]])
im = plt.imshow(step(), cmap=CM, interpolation='none')
 
def updatefig(*args):
    im.set_array(step())
    return im,
 
ani = animation.FuncAnimation(fig, updatefig, interval=5, blit=True)
plt.axis('off')
plt.show()
