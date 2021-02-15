import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

maxRange = int(input())
for i in range(2,maxRange + 1):
    if isPrime(i) == True:
        print(i, end = ", ")

# Sieve of Eratosthenes

maxRange = int(input())
arr = [False for _ in range(maxRange + 1)]
print(arr)
for i in range(2, int(math.sqrt(maxRange)) + 1):
    if (arr[i] == False):
        for j in range(i+i, int(maxRange) + 1, i):
            arr[j] = True
for i in range(2, (maxRange + 1)):
    if arr[i] == False:
        print(i, end = ", ")