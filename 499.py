# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:04:45 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
n = bin(n).replace('0b', '')
if n.count('0') == 0:
    print(-1)
else:
    print(n.count('1')//n.count('0'))