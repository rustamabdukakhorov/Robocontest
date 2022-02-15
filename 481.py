# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 18:00:50 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
m = [pow(int(i),len(str(n))) for i in str(n)]
if sum(m) == n:
    print(sum([int(i) for i in str(n)]))
else:
    print(n)