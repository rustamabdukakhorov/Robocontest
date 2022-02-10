# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:04:11 2022

@author: R.U.S.T.E.A.M
"""

a, b = map(int, input().split())
if b%100 + b == 1932:
    print(2022-a, 2022-b)
else:
    print('NO')