# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 17:38:42 2022

@author: R.U.S.T.E.A.M
"""

n, m = map(int, input().split())
if m%2 == 1:
    print(-1)
else:
    print(n + m//2 + 1)