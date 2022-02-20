# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 22:37:37 2022

@author: R.U.S.T.E.A.M
"""

a = int(input())
b = int(input())
i = 1
while a&i != b&i:
    i = i*2
print(i)