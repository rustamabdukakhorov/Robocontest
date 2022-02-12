# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:07:50 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
l = list(map(int, input().split()))
j = [i for i in l if i%2==0]
if j:
    print(max(j))
else:
    print(-1)