# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:37:36 2022

@author: R.U.S.T.E.A.M
"""

a,b,c = map(int, input().split())
x = abs(a-c)
y = abs(b-c)
if x == y:
    print('sichqon')
elif x<y:
    print('1-mushuk')
else:
    print('2-mushuk')