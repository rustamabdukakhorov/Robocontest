# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:10:28 2022

@author: R.U.S.T.E.A.M
"""

year = int(input())
years = str('0'*(4-len(str(year))))+str(year)
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print("12/09/"+years)
else:
    print("13/09/"+years)