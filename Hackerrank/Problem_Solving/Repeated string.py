#!/bin/python3
## https://www.hackerrank.com/challenges/repeated-string/problem
import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    R = n%l
    Q = n//l
    S = ""
    # if l == 1 or len(set(s)) == 1:   ## Memory error for larger inputs
    #     return n
    # S = s*Q
    # s = S+s[:R]
    # print(s.count("a"))
    # return s.count("a")
    
    c = s.count("a")
    return c*Q+(s[:R].count("a"))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
