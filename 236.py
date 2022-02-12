# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 09:54:42 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())

if n<0:
    print(-1 * (abs(n)*(abs(n)+1))//2 + 1)
else:
    print(n*(n+1)//2)