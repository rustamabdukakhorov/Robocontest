# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:29:00 2022

@author: R.U.S.T.E.A.M
"""

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
a = ((x1-x2)**2 + (y1-y2)**2)**0.5
b = ((x3-x2)**2 + (y3-y2)**2)**0.5
c = ((x1-x3)**2 + (y1-y3)**2)**0.5
if a+b > c and a+c > b and b+c > a:
    print('uchburchak')
else:
    print('uchburchak emas')