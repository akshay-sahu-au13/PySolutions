
dp = [[-1 for _ in range(100)] for _ in range(100)]
def Solve(A, B, idx1, idx2):
 
    if idx1 >= len(A):
        return 0
 
    if idx2 >= len(B):
        return 0
 
    if dp[idx1][idx2] != -1:
        return dp[idx1][idx2]
 
    if A[idx1] == B[idx2]:
        return 1 + Solve(A, B, idx1 + 1, idx2 + 1)
 
    ans = max(
        Solve(A, B, idx1, idx2 + 1),
        Solve(A, B, idx1 + 1, idx2)
    )
    dp[idx1][idx2] = ans
    return ans
 
 
if __name__ == "__main__":
    print(Solve("ABCKLRT", "RCBKRT", 0, 0))