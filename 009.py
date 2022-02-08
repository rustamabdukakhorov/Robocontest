# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:12:51 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = list(map(int, input().split()))
for i in a:
    if a.count(i) == 1:
        print(i)
        break