# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 22:52:56 2022

@author: R.U.S.T.E.A.M
"""

a = list(map(int, input().split()))
s = int(input())
print(max(0, s-sum(a)))