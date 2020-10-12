## https://leetcode.com/problems/sort-array-by-parity-ii/

# Sample Input/Output
# Input: [4,2,5,7]
# Output: [4,5,2,7]

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        res = []
        
        x = 0
        for i in A:
            if i % 2 == 0:
                res.insert(x,i)
                x+=2
        x = 1
        for j in A:
            if j % 2 == 1:
                res.insert(x,j)
                x += 2
            
        return res
        