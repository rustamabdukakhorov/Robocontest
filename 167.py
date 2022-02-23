# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:08:04 2022

@author: R.U.S.T.E.A.M
"""

n, p = map(int, input().split())
res = min(n//2 - p//2, p//2)
print(res)