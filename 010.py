# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:14:06 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
l = list(map(int, input().split()))
if sum(l) > n:
    print("Yes")
else:
    print("No")