#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    pivot = n-1
    
    # while pivot > 0:
    pivot_value = arr[pivot]
    i = pivot-1
    
    while i >= 0 and arr[i] > pivot_value:
        arr[i+1] = arr[i]
        print(*arr)
        i -= 1
        
    arr[i+1] = pivot_value
    print(*arr)
    pivot -= 1
        
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
