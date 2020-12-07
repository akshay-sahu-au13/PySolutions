#!/bin/python3
## https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
import sys


S = input().strip()
try:
    print(int(S))
except:
    print("Bad String")