# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 12:39:15 2022

@author: R.U.S.T.E.A.M
"""

def mostFrequent(arr, n):
    arr.sort()
    max_count = 1; curr_count = 1
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count += 1
             
        else :
            if (curr_count > max_count):
                max_count = curr_count
            curr_count = 1
    if (curr_count > max_count):
        max_count = curr_count
    return max_count
n = int(input())
a = list(map(int, input().split()))
print(mostFrequent(a, n))
