# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:03:39 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
s = 0
if n>=100:
    s += n//100
    n%=100
if n>=20:
    s += n//20
    n%=20
if n>=10:
    s += n//10
    n%=10
if n>=5:
    s += n//5
    n%=5
if n>=1:
    s += n
print(s)
