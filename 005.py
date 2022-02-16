# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:15:25 2022

@author: R.U.S.T.E.A.M
"""

import math
n = int(input())
k = 0
if n == 0:
    print(-1)
else:
    if n<0:
        n = -n
        q = int(n**0.5)
        if q**2 == n:
            k = -1
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            k+=2
    print(k)