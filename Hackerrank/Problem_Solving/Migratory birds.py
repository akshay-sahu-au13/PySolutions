#!/bin/python3
#$### https://www.hackerrank.com/challenges/migratory-birds/problem

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    d = {}
    arr.sort()
    for i in arr:

        if i not in d:
            d[i] = 1
        else:
            d[i] +=1
        
    return max(d, key=d.get)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
