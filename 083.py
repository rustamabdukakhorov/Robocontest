# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:06:26 2022

@author: R.U.S.T.E.A.M
"""

s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
m = list(map(int, input().split()))
n = list(map(int, input().split()))
a = [i for i in m if i>0 and i+a>=s and i+a<=t]
b = [i for i in n if i<0 and i+b<=t and i+b>=s]
print(len(a))
print(len(b))