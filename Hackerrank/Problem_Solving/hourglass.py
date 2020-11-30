#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
## https://www.hackerrank.com/challenges/2d-array/problem
def hourglassSum(arr):
    hg = []

    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hgsum = sum(arr[i][j : j+3]) + arr[i+1][j+1] + sum(arr[i+2][j : j+3])
            hg.append(hgsum)
    return max(hg)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
