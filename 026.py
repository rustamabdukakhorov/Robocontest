# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 00:18:39 2022

@author: R.U.S.T.E.A.M
"""
mod = 1000000007
t = int(input())
x = []
for i in range(t):
    n = int(input())
    x.append(n)
for i in x:
    print(i*i % mod)