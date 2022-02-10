# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 10:00:49 2022

@author: R.U.S.T.E.A.M
"""

wint = [12,1,2]
spri = [3,4,5]
summ = [6,7,8]
autm = [9,10,11]

n = int(input())
if n in wint:
    print('Winter')
elif n in spri:
    print('Spring')
elif n in summ:
    print('Summer')
elif n in autm:
    print('Autumn')
else:
    print('Error')