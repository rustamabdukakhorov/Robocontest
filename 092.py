# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 07:36:58 2022

@author: R.U.S.T.E.A.M
"""

def sana(a, n):
    a.sort()
    count = 1
    res = 0
    for i in range(1,n):
        if a[i] == a[i-1]:
            count += 1
        else:
            res += count - count%2
            count = 1
    return res + count - count%2

t = int(input())
x = []
for i in range(t):
    n = int(input())
    m = list(map(int, input().split()))
    x.append(sana(m,n))
for i in x:
    print(i)