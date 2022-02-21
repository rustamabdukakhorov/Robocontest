# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:56:28 2022

@author: R.U.S.T.E.A.M
"""

n, k = map(int, input().split())
m = list(map(int, input().split()))
m.sort()
res = 0
for i in m:
    res += i>0 and i>=m[-k]
print(res)