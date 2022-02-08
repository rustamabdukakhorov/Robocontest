# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:17:41 2022

@author: R.U.S.T.E.A.M
"""

n,k = map(int, input().split())
M = int(1e9+7)
a = pow(k, n, M)-1
b = pow(k-1, M-2, M)
print((a*b)%M)