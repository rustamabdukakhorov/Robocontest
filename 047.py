# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:15:01 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
x = []
for i in range(n):
    a = input()
    a = bin((int(a)))
    x.append(a.count('1'))
for i in x:
    print(i)