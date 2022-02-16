# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:44:22 2022

@author: R.U.S.T.E.A.M
"""

word = input()
letter = ['sh','ch','ng']
nword = []
i = 0
while i <= len(word)-1:
    if word[i:i+2] in letter:
        nword.append(word[i:i+2])
        i += 2
    else:
        nword.append(word[i])
        i += 1
print(''.join(nword[::-1]))