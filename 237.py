# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:57:47 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
l = list(map(int, input().split()))
l.sort()
x = []
for i in l:
    if not i in x:
        x.append(i)
print(sum([l.count(i)//2 for i in x]))