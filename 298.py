# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:07:25 2022

@author: R.U.S.T.E.A.M
"""

n, m = map(int, input().split())
a, b = [], []
for i in range(2*n):
    if i<n:
        a.append(list(map(int, input().split())))
    else:
        b.append(list(map(int, input().split())))
c = []
for i in range(n):
    x = []
    for j in range(m):
        x.append(a[i][j] + b[i][j])
    c.append(x)
for i in c:
    print(' '.join([str(j) for j in i]))