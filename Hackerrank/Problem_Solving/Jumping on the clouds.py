#!/bin/python3
## https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i =  0
    steps = 0
    while i < len(c)-1:
        if i+2< len(c) and c[i+2] != 1:
            steps += 1
            i += 2
        else:
            steps += 1
            i += 1
    return steps
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
