# -*- coding: utf-8 -*-
"""
Created on Mon Feb 14 12:24:42 2022

@author: R.U.S.T.E.A.M
"""

def isPrime(num):
    for i in range(2,num):  
       if (num % i) == 0:  
           return False
       else:  
           continue
    return True

def digSum(n):
    return sum([int(i) for i in str(n)])

def isSmith(num):
    n = num
    div_sum = []
    div_degree = []
    i = 2
    while num > 1:
        if num%i == 0 and isPrime(i):
            num //= i
            if not i in div_sum:
                div_sum.append(i)
                div_degree.append(1)
            else:
                div_degree[-1] = div_degree[-1]+1
        else:
            i += 1
            continue
    s = 0
    for i in range(len(div_sum)):
        s += digSum(div_sum[i])*div_degree[i]
    if s == digSum(n):
        return 1
    else:
        return 0

n = int(input())
print(isSmith(n))