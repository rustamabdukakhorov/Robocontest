# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:36:10 2022

@author: R.U.S.T.E.A.M
"""

number = list(map(int, input().split()))
word = input()
h = max([number[ord(i)-97] for i in word])
print(len(word) * h)