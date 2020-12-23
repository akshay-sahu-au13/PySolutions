## https://leetcode.com/problems/shuffle-string

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(indices)
        shuffled = [0]*n
        
        for i in range(n):
            shuffled[indices[i]] = s[i]
        
        return "".join(shuffled)