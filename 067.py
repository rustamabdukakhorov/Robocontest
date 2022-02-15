# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 07:19:45 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())

if n >= 0:
    n = bin(n).replace('0b', '')
else:
    n = bin(2**32 - 1 + (n + 1)).replace('0b', '')

n = (32 - len(n))*'0' + n
print(n)