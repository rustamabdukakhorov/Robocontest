# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:56:26 2022

@author: R.U.S.T.E.A.M
"""

x = []
for i in range(7):
    l = list(map(int, input().split()))
    x.append(l)
    for j in l:
        if j == 1:
            k = [i, l.index(1)]
print(sum([abs(i - 3) for i in k]))