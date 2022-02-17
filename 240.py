# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:58:22 2022

@author: R.U.S.T.E.A.M
"""

t = int(input())
x = []
for i in range(t):
    n = int(input())
    x.append((n+1)//2)
for i in x:
    print(i)