# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 19:21:02 2022

@author: R.U.S.T.E.A.M
"""

y = int(input())

if (y%400 == 0) or (y%4 == 0 and y%100 != 0):
    print("Kabisa yili")
else:
    print("Kabisa yili emas")