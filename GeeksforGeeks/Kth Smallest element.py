#https://practice.geeksforgeeks.org/problems/kth-smallest-element/
for i in range(int(input())):
    N = int(input())
    Ar = list(map(int,input().split()))
    k = int(input())
    Min = Ar[-1]
    Ar.sort()
    print(Ar[k-1])
        
        