#!/bin/python3
## https://www.hackerrank.com/challenges/append-and-delete/problem
import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    ls =len(s)
    lt =len(t)
    if k >= ls + lt:
        return "Yes"
    elif k < abs(lt-ls):
        return "No"
    else:
        i = 0
        while i < ls-1 and i < lt-1 and s[i] == t[i]:
            # if i < ls-1 and i < lt-1:
                i += 1
        
        if ls>=lt and k >= ls-i + lt-i:
            return "Yes"
        elif lt>ls and k%2 == (ls-i + lt-i)%2:
            return "Yes"
        else:
            return "No"
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
