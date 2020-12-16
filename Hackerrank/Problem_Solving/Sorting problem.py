#!/bin/python3
## https://www.hackerrank.com/challenges/30-sorting/problem
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
count = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i] > a[j]:
            a[i],a[j] = a[j],a[i]
            count += 1
        else:
            continue

print(f"Array is sorted in {count} swaps.")
print("First Element:", a[0])
print("Last Element:", a[-1])
