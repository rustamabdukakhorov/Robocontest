# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:15:51 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[-2])