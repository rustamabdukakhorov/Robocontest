# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:31:57 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
if n>37:
    if n%5 < 3:
        print(n)
    else:
        print((n//5 + 1)*5)
else:
    print(n)