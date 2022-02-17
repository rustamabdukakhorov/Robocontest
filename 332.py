# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:17:11 2022

@author: R.U.S.T.E.A.M
"""

s = input()
x = int(input())
h, m = int(s[:2]), int(s[3:])
if h == 23 and m == 59:
    print(-1)
else:
    k = 0
    while (h//10 + h%10 + m//10 +m%10)%x != 0:
        m += 1
        k += 1
        if m>=60:
            h += 1
            m = m%60
    print(k)