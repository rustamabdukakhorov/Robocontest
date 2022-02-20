# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 22:58:33 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
count = 0
while n!=1:
    if n%3 == 0:
        n = n//3
        count += 1
    elif n%3 == 2:
        n = 2*n-1
        count += 1
    else:
        n = 2*n+1
        count += 1
print(count)