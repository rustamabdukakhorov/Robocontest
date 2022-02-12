# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 15:55:50 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x**3 + x)
for i in a:
    print(i)