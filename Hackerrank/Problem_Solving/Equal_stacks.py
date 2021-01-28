#!/bin/python3
## https://www.hackerrank.com/challenges/equal-stacks/problem
import math
import os
import random
import re
import sys
from collections import defaultdict
#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
# def equalStacks(h1, h2, h3, maxH):
#     # Write your code here
#     # maxH = []
#     if not h1 or not h2 or not h3:
#         return
    
#     # while h1 and h2 and h3:
#     if sum(h1) == sum(h2) == sum(h3):
#         maxH.append(sum(h1))
#     else:
#         equalStacks(h1[1:], h2, h3, maxH)
#         equalStacks(h1, h2[1:], h3, maxH)
#         equalStacks(h1, h2, h3[1:], maxH)
#     return max(maxH) if maxH else 0

def equalStacks(h1, h2, h3):
    h11 = defaultdict(int)
    h22 = defaultdict(int)
    h33 = defaultdict(int)
    
    
    rs1,rs2,rs3 = 0,0,0
    for i in range(len(h1)-1,-1,-1):
        rs1 += h1[i]
        h11[rs1] = "x"
    for j in range(len(h2)-1,-1,-1):
        rs2 += h2[j]
        if h11[rs2]:
            h22[rs2] = "x"    
    for k in range(len(h3)-1,-1,-1):
        rs3 += h3[k]
        if h22[rs3]:
            h33[rs3] = "x"
            
    # print(h11, h22, h33)
    return max(h33.keys()) if h33 else 0
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    maxH = []

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3) ## result = equalStacks(h1, h2, h3, maxH)

    fptr.write(str(result) + '\n')

    fptr.close()
