# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:12:26 2022

@author: R.U.S.T.E.A.M
"""

arr = list(map(int, input().split()))
print(sum(arr) - max(arr), sum(arr) - min(arr))