# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:23:28 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
s = 0
for i in range(n-1):
    a,b = map(int, input().split())
    s += a-b
m = int(input())
if s>=m:
    print(m-s)
else:
    print(0)