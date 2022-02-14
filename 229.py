# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 20:35:03 2022

@author: R.U.S.T.E.A.M
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 19:46:35 2022

@author: R.U.S.T.E.A.M
"""

a, b = map(float, input().split())
a, b = (a+b)/2 , (a*b)**0.5
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('=')
else:
    print('<')