# https://www.hackerrank.com/contests/c-v-raman-fprt-july-seta/challenges/array-replacement-4

def smallestInt(A, N):
    arr = [0]*N
    # arr[0] = 0

    for i in range(1, N):
        arr[i] = min(A[:i])
        # print(arr)
    return arr


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    print(*smallestInt(A, N))
