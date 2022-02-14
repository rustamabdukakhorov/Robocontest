# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:19:35 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
for i in range(1,n+1):
    t = True
    k = i%100
    if k + i != n:
        t = False
    if t:
        print(i,end=' ')