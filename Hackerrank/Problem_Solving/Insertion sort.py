#!/bin/python3

import math
import os
import random
import re
import sys
# 5
# 2 4 6 8 3

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    for i in range(1,n):
        key = arr[i] #3
        j = i-1 #3
        while j>=0 and key < arr[j]: 
            arr[j+1] = arr[j]
            print(*arr)
            j-=1
        arr[j+1] = key
    print(*arr)
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
