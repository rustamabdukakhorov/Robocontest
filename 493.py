# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 06:25:34 2022

@author: R.U.S.T.E.A.M
"""

t = int(input())
x = []
for i in range(t):
    a,b,n = map(int, input().split())
    a, b = a-n, b-n
    if a == 0 and b == 0:
        x.append('Draw!')
    elif a >= 0 and b >= 0:
        if a > b:
            x.append('Azimjon')
        else:
            x.append('Maqsud')
    elif a >= 0 and b < 0:
        x.append('Maqsud')
    elif a < 0 and b < 0:
        x.append('Draw!')
    elif a < 0 and b >= 0:
        x.append('Azimjon')
    else:
        x.append('Draw!')
for i in x:
    print(i)