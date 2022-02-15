# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 22:18:17 2022

@author: R.U.S.T.E.A.M
"""

import math
n, m = map(int, input().split())
x = 0
for i in range(m):
    l,r,k = map(int,input().split())
    x += (r+1-l)*k
print(math.floor(x//n))