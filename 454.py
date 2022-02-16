# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:51:49 2022

@author: R.U.S.T.E.A.M
"""

sys = {
       '0' : '0',
       '1' : '1',
       '2' : '2',
       '3' : '3',
       '4' : '4',
       '5' : '5',
       '6' : '6',
       '7' : '7',
       '8' : '8',
       '9' : '9',
       '10' : 'A',
       '11' : 'B',
       '12' : 'C',
       '13' : 'D',
       '14' : 'E',
       '15' : 'F'
       }
k, n = map(int, input().split())
result = []
while True:
    result.append(sys.get(str(k%n)))
    k //= n
    if k == 0:
        break
print(''.join(result[::-1]))