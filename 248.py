# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 21:27:08 2022

@author: R.U.S.T.E.A.M
"""

import math

def son(n,k):
    return n + math.floor((n-1)/(k-1))

n, k = map(int, input().split())

print(son(n, k))