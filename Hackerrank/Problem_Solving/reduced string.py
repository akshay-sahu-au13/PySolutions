#### https://www.hackerrank.com/challenges/reduced-string/problem
#!/bin/python3

import math
import os
import random
import re
import sys

 
################################################
def superReducedString(s):
    lst = []
    for i in s:
        if i not in lst:
            lst.append(i)
        
        elif lst[-1] == i:
            lst.pop()

        else:
            lst.append(i)
                
    if len(lst) == 0:
        return "Empty String"
    else:
        return "".join(lst)
##########################################################
### USING RECURSION ###

def superReducedString(s):
    for i in range(len(s)-1):
        if len(s)==2 and s[i]==s[i+1]:
            return "Empty String"
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
            return superReducedString(s)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
