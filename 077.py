# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 21:13:20 2022

@author: R.U.S.T.E.A.M
"""

import math
x, y = map(float, input().split())
n = math.ceil((100-x)/(x-3*y))
print(n + 1)