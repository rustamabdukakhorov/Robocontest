# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 20:06:21 2022

@author: R.U.S.T.E.A.M
"""

def tak(s):
    a = [s[i] for i in range(len(s))]
    a.sort()
    x = [a[0]]
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            x.append(a[i+1])
    return len(x)
n = int(input())
x = []
for i in range(n):
    x.append(input())
for i in x:
    print(len(i)-tak(i))