# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 13:55:59 2020

@author: Sareh
"""
import numpy as np

a=np.array([[0,0],
            [1,0]],
        dtype=float)


    

def rowequi(a):


    for j in range(len(a[:,0])):
        for i in range(len(a[0,:])):
            if a[j,i]!=0:
                a[j]=(1/a[j][i])*a[j]
                for t in range(len(a[:,0])):
                    if t!=j:
                        a[t]=a[t]-a[t][i]*a[j]
                break
    return a
            


print(rowequi(a))
