# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:01:56 2022

@author: R.U.S.T.E.A.M
"""

n = float(input())
a, b = map(float, input().split())
if int(a*10)%5 == 0 and int(b*10)%5 == 0 and a+b == n:
    print('YES')
else:
    print('NO')