# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:19:24 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
x = [0,0,0]
x[2] = (2 - len(str(n%60)))*'0' + str(n%60)
x[1] = (2 - len(str(n//60 % 60)))*'0' + str(n//60 % 60)
x[0] = str(n//3600 % 24)
print(':'.join(x))
