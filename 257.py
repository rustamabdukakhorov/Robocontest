# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:35:55 2022

@author: R.U.S.T.E.A.M
"""

s = input()
l = s.split('0')
if s.count('1') == len(max(l)):
    print('YES')
else:
    print('NO')