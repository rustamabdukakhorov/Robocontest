# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:16:45 2022

@author: R.U.S.T.E.A.M
"""

a, b = map(int, input().split())
if a >= 0 and b >= 0:
    if a > 0:
        s = 1 + b
    else:
        s = 1
    print(s)