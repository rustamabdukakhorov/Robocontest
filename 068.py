# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:12:33 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = list(map(int, input().split()))
k = int(input())
a.sort()
print(a[k-1])