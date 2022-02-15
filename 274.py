# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:18:21 2022

@author: R.U.S.T.E.A.M
"""

n, k = map(int, input().split())
l = list(map(int, input().split()))
hamyon = int(input())
s = 0
for i in range(n):
    if i != k:
        s += l[i]
if hamyon >= s//2:
    print(hamyon - s//2)
else:
    print(0)