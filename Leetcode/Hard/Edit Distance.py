## https://leetcode.com/problems/edit-distance/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        Ar = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        
        for i in range(len(word1) + 1):
            Ar[i][0] = i
        for j in range(len(word2) + 1):
            Ar[0][j] = j
            
        for i in range(1,len(word1) + 1):
            for j in range(1,len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    Ar[i][j] = Ar[i-1][j-1]
                else:
                    Ar[i][j] = 1 + min(Ar[i-1][j-1], Ar[i-1][j], Ar[i][j-1])
        
        return Ar[-1][-1]