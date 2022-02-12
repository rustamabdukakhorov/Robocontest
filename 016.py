# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 14:05:13 2022

@author: R.U.S.T.E.A.M
"""

bir = {
       '1' : 'bir ',
       '2' : 'ikki ',
       '3' : 'uch ',
       '4' : 'to\'rt ',
       '5' : 'besh ',
       '6' : 'olti ',
       '7' : 'yetti ',
       '8' : 'sakkiz ',
       '9' : 'to\'qqiz ',
       '0' : ''
       }
on = {
      '1' : 'o\'n ',
      '2' : 'yigirma ',
      '3' : 'o\'ttiz ',
      '4' : 'qirq ',
      '5' : 'ellik ',
      '6' : 'oltmish ',
      '7' : 'yetmish ',
      '8' : 'sakson ',
      '9' : 'to\'qson ',
      '0' : ''
      }
m = int(input())
a = str(m)
w = a[::-1]
x = []
while m>0:
    n = m%1000
    s = ''
    if n//100:
        s += (bir.get(str(n//100)) + 'yuz ')
    if (n//10) % 10:
        s += (on.get(str(n//10 % 10)))
    if n%10:
        s += (bir.get(str(n%10)))
    m=m//1000
    x.append(s)
    
if len(x)>=2 and sum([int(i) for i in w[3:6]]) > 0:
    x[1] += 'ming'
if len(x)>=3 and sum([int(i) for i in w[6:9]]) > 0:
    x[2] += 'million'
if len(x)>=4 and sum([int(i) for i in w[9:13]]) > 0:
    x[3] += 'milliard'
print(' '.join(x[::-1]))