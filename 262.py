# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 18:23:12 2022

@author: R.U.S.T.E.A.M
"""

import math
phone = input()
number = [int(i) for i in phone[5:]]
number.sort()
count, result = 1, 1
for i in range(1,7):
    if number[i] == number[i-1]:
        count += 1
    else:
        result *= math.factorial(count)
        count = 1
result *= math.factorial(count)
print(math.factorial(7)//result)