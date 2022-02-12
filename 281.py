# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:07:23 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = list(map(int, input().split()))

a.sort()

x = [a[0]]

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        x.append(a[i+1])
print(len(a) - max([a.count(i) for i in x]))