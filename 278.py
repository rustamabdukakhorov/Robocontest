# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:15:53 2022

@author: R.U.S.T.E.A.M
"""

import math
n = int(input())
x = (math.floor(math.log2(math.ceil(n/3))))
print(3*2**x +1 - (n - 3*(2**x - 1)))