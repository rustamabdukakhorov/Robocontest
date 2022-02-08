# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:11:39 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = [2, 2]
for i in range(2,46):
    a.append(a[i-1] + a[i-2])
print(a[n-1])