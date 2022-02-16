# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 18:16:27 2022

@author: R.U.S.T.E.A.M
"""

s = input()
s = [i for i in s]
if len(s)>1:
    for i in range(1,len(s),2):
        s[i-1], s[i] = s[i], s[i-1]
result = ''
for i in range(len(s)):
    result += chr(219 - ord(s[i]))
print(result)