#code
# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/
for i in range(int(input())):
    N = int(input())
    A = list(map(int,input().split()))
    
    cur,l,r = 0,0, N-1
    while cur<=r:
        if A[cur] == 0:
            A[cur],A[l] = A[l],A[cur]
            cur += 1
            l += 1
        elif A[cur] == 2:
            A[cur],A[r] = A[r],A[cur]
            # cur += 1
            r -= 1
        else:
            cur+=1
    print(*A)