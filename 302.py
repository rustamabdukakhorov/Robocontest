# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 19:39:24 2022

@author: R.U.S.T.E.A.M
"""

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = input()

for i in s:
    print(i,word.count(i))