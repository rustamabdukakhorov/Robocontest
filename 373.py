# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 12:08:00 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
s = str(n)
if len(s) == 6:
    if int(s[0])+int(s[1])+int(s[2])==int(s[3])+int(s[4])+int(s[5]):
        print('YES')
    else:
        print('NO')
else:
    print('NO')