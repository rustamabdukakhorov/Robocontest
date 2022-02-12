# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 20:57:24 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
n %= 50
n+=1
if 0<n<=25:
    print('O__')
if 25<n<=29:
    print('OO_')
if 29<n<=35:
    print('_O_')
if n>35:
    print('__O')