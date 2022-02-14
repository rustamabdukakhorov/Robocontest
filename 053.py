# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:22:55 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())

if n == 1 or n == 2:
    print(0)
else:
    print(n*(n-3) // 2)