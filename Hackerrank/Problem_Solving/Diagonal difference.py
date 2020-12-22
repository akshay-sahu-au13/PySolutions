#!/bin/python3

import math
import os
import random
import re
import sys
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    d = 0
    ad = 0
    n = len(arr)
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if i == j:
#                 d += arr[i][j]
#             elif 
#                 ad = arr[]

    for i in range(n):
        d += arr[i][i]
        ad += arr[i][n-i-1]
    # print(d,ad)
    return abs(d-ad)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
