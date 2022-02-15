# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:05:05 2022

@author: R.U.S.T.E.A.M
"""

a, b, c, x = map(int, input().split())
d = b**2 - 4*a*c
if d < 0:
    print('NO')
else:
    d = d**0.5
    if x == (-b+d)//(2*a) or x == (-b-d)//(2*a):
        print('YES')
    else:
        print('NO')