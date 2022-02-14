# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:17:47 2022

@author: R.U.S.T.E.A.M
"""

t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))
print((t2[0] - t1[0])*3600 + (t2[1] - t1[1])*60 + (t2[2] - t1[2]))