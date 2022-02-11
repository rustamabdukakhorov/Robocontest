# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 11:48:37 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
s = input()
a = ''
for i in s:
    k = ord(i)
    if k>=97 and k<=122:
        a += chr((k + n - 97)%26 + 97)
    elif k>=65 and k<=90:
        a += chr((k + n - 65)%26 + 65)
    else:
        a += i
print(a)