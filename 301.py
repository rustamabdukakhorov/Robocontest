# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 09:50:03 2022

@author: R.U.S.T.E.A.M
"""
def imtihon(n, l):
    for i in range(n-1):
        if l[i] > l[i+1]:
            return 'NO'
    return 'YES'
n = int(input())
a = list(map(int, input().split()))
print(imtihon(n, a))