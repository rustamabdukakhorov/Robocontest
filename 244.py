# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 10:25:47 2022

@author: R.U.S.T.E.A.M
"""

n, m = map(int, input().split())
if 1 in [n,m]:
    print(max(n,m) - 1)
else:
    print(min(m,n) - 1 + (max(n,m) - 1)*min(m,n))