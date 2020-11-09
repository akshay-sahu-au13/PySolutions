#!/bin/python3
## https://www.hackerrank.com/challenges/cut-the-sticks/copy-from/187269711
import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    res = []
    arr.sort()
    
    for i in range(len(arr)):
        res.append(len(arr))
        arr = [i-arr[0] for i in arr]
        # print(arr)
        if (len(arr) == 1 and arr[0] == 0):
            return res
        elif len(arr) == 0:
            return res[:-1]
        while len(arr) and arr[0] == 0:
            arr.pop(0)
    # print(res)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
