# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:03:29 2022

@author: R.U.S.T.E.A.M
"""

n, k = map(int, input().split())
for i in range(k):
    if n and n%10 == 0:
        n//=10
    elif not n:
        n = 0
        break
    else:
        n -= 1
print(n)