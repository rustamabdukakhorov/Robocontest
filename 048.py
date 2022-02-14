# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:21:56 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())

number = 1

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(number, end = ' ')
        number = number + 1
    print()