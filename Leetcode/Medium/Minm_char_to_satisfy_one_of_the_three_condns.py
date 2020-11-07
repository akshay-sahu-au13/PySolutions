    def minCharacters(self, a: str, b: str) -> int:
        A = [0]*26  # freq of each alphabet in a
        B = [0]*26  
        for ch in a:
            A[ord(ch) - ord('a')] += 1
        for ch in b:
            B[ord(ch) - ord('a')] += 1
        res = len(a) - max(A) + len(b) - max(B) # condition 3 met
        sumA, sumB = len(a), len(b)
        runA, runB = 0, 0 # running total
        for i in range(25):
            runA += A[i]
            runB += B[i]
            res = min(res, min(runA + sumB - runB, runB + sumA - runA))
        return res