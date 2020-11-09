#!/bin/python3
## https://www.hackerrank.com/challenges/sherlock-and-squares/problem
import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    count = 0
    R = range(a,b+1)
    # for i in R:
    #     root = i**0.5
    #     if str(root)[-1] == "0":
    #         count += 1
    # return count

    r1 = int(a**0.5)
    while r1**2 <= b:
        if r1**2 in R:
            count += 1
        r1 += 1
    return count  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
