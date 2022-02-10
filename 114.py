# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:08:21 2022

@author: R.U.S.T.E.A.M
"""

x1, v1, x2, v2 = map(int, input().split())

def kin(s1,v1,s2,v2):
    for i in range(10000):
        if (s1 + v1*i) == (s2 + v2*i):
            return 'YES'
    return 'NO'

print(kin(x1,v1,x2,v2))