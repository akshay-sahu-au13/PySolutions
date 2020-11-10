#!/bin/python3
## https://www.hackerrank.com/challenges/minimum-distances/problem
import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    
    L  =len(a)
    dist = L
    for i in range(L):
        for j in range(i+1,L):
            if a[i] == a[j] and j-i < dist:
                dist = j-i
                
    return dist if dist<L else -1
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
