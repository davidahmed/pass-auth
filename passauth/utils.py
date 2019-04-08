#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 15:42:47 2019

@author: admin
"""
import pandas as pd
import matplotlib.pyplot as plt


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

