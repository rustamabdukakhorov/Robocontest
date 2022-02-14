# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:16:49 2022

@author: R.U.S.T.E.A.M
"""

l = list(map(int, input().split()))
s = 0
for i in range(len(l)):
    s += l[i]//2 + l[i]%2
print(s)