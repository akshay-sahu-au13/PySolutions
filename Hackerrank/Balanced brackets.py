#!/bin/python3
## https://www.hackerrank.com/challenges/balanced-brackets/problem
import math
import os
import random
import re
import sys

# Complete the isBalanced function below.

def isBalanced(s):
    m = {1:"()", 2:"{}", 3: "[]"}
    stack = [s[0]] ## {[()]}
    for i in range(1, len(s)):
        if stack:
            if stack[-1] + s[i] in m.values():
                stack.pop()
            else:
                stack.append(s[i])
        else:
            stack.append(s[i])        
        # print(stack)    
    return ("YES" if not len(stack) else "NO")
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
