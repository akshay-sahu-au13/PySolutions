#!/bin/python3
## https://www.hackerrank.com/challenges/equality-in-a-array/problem
import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i]+= 1
        else:
            d[i] = 1
    return len(arr) - max(d.values())
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
