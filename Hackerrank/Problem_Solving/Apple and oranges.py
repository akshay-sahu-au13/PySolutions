###https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=internal-search

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple = 0
    orange = 0
    for i in range(m):
        if s <= (a + apples[i]) <= t:
            apple += 1
    for j in range(n):
        if s <= (b+ oranges[j]) <= t :
            orange += 1
    print(apple)
    print(orange)
    

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
