# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 12:37:16 2022

@author: R.U.S.T.E.A.M
"""
a,b,m = map(int, input().split())

if m == 0:
    print(a)
elif m == 1:
    print(b)
else:
    print(a | b)