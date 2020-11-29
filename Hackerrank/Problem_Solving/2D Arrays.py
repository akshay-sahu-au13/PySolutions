#!/bin/python3
## https://www.hackerrank.com/challenges/30-2d-arrays/problem
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    hg = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hgsum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            hg.append(hgsum)
    print(max(hg)) 
    
