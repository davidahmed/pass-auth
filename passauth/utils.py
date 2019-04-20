#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:42:47 2019

@author: admin
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math


def plotUserMouse3D(mouseMovement):
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    ax = plt.subplot(2,2,1, projection='3d')
    #ax.scatter3D(user1_mouseMovement[0], user1_mouseMovement[1], user1_mouseMovement[2], c=user1_mouseMovement[2], cmap='Greens');
    ax.plot3D(mouseMovement[0], mouseMovement[1], mouseMovement[2])


def plotUserMouseScatter(mouseMovements, figno):
    color = mouseMovements[2]/max(mouseMovements[2])
    plt.figure(figsize=(10,10), dpi=80)
    plt.subplot(*figno)
    plt.ylim([0,500])
    plt.xlim([0,1200])
    plt.scatter(mouseMovements[0], mouseMovements[1], c=color, s=color*500, alpha=0.3)

    
def plotUserMouseScatterMultiple(user, n=5):
    for i in range(n):
        plotUserMouseScatter(pd.DataFrame(user[i]['mouseMovements']), (10,1,i+1))



def pad(arr, n):
    """
    If arr is not equal to n in length, fill it with zero
    
    >>>pad([1, 1], 5)
    [1, 1, 1, 1, 1]
    """
    if n == None:
        arr
    if n < len(arr):
        arr = arr[:n]
        
    else:
        arr = arr + ((n-len(arr)) * [len(arr[-1]) * [0]])
        #arr = arr + ((n-len(arr)) * [arr[-1]])
        
    return arr


def logify(event):
    return [event[0]* math.log(event[2]+1), event[1]* math.log(event[2]+1)]


def normalize(arr):
    arr = np.array(arr)
    mean = arr.mean()
    std = arr.std()
    return (arr-mean)/std
  
    
def bin(arr):
    return np.histogram(arr, range=(-100,100), bins=100)[0]