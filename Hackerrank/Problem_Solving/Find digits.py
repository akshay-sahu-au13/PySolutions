#!/bin/python3
## https://www.hackerrank.com/challenges/find-digits/problem
import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    x = n
    count = 0
    while x != 0:
        d = x%10
        if d and n%d == 0:
            count += 1
        x //= 10
    return count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
