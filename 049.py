# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 13:45:30 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
l = list(map(int, input().split()))
r = ''
for i in l:
    if (int((8*i + 1)**0.5))**2 == 1 + 8*i:
        r += '1'
    else:
        r += '0'
print(r)