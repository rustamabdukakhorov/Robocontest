# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:38:15 2022

@author: R.U.S.T.E.A.M
"""

a = input()
print(len(a))
for i in a:
    n = ord(i)
    x = ''
    while n>=1:
        x += str(n%2)
        n = n//2
    print(x[::-1])