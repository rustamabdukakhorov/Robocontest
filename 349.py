# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 17:47:39 2022

@author: R.U.S.T.E.A.M
"""

n = int(input())
import math
def primefactors(n):
   while n % 2 == 0:
      print (2, end=' ')
      n = n / 2
    
   for i in range(3,int(math.sqrt(n))+1,2):
     
      while (n % i == 0):
         print (round(i), end=' ')
         n = n // i
    
   if n > 2:
      print (round(n))
      
primefactors(n)