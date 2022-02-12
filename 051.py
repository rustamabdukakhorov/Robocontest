# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:50:00 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = []
for i in range(n):
    x = int(input())
    k = bin(x).count('1')
    a.append(k)
for i in a:
    print(i)