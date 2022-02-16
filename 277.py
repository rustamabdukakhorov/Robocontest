# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 19:17:18 2022

@author: R.U.S.T.E.A.M
"""

def compete(array, k):
    array = [i for i in array if i<=0]
    if len(array) >= k:
        return 'Qizg\'in'
    else:
        return 'Zerikarli'
t = int(input())
result = []
for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    result.append(compete(l, k))
for i in result:
    print(i)