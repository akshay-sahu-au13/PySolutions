#!/bin/python3
## https://www.hackerrank.com/challenges/30-binary-numbers/problem
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    res = []
    count  = 0
    n = int(input())
    def DecimalToBinary(n): 
      
        if n > 1: 
            DecimalToBinary(n // 2) 
        res.append(n % 2)
    DecimalToBinary(n)    
    i = 0
    Max = 0
    while i < len(res):
        
        if res[i] == 1:
            count+=1
            Max = max(Max,count)
        else:
            count = 0
        i += 1
        
    print(Max)