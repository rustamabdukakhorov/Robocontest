# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:39:17 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
s = 0
while n>0:
  s+=n%10
  n//=10
print(s)