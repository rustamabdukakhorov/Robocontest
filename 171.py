# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:15:15 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
a = list(map(int, input().split()))
left = [i for i in a if i<0]
right = [i for i in a if i>0]
left, right = abs(sum(left)), abs(sum(right))
print(abs(left-right))