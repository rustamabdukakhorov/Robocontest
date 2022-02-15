# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:30:33 2022

@author: R.U.S.T.E.A.M
"""

def satr(s):
    x = []
    for i in range(len(s)-1):
        x.append(abs(ord(s[i]) - ord(s[i+1])))
    if x == x[::-1]:
        return 'Ajoyib satr'
    else:
        return 'Oddiy satr'
n = int(input())
result = []
for i in range(n):
    s = input()
    result.append(satr(s))
for i in result:
    print(i)