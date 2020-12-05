## https://leetcode.com/problems/counting-bits/
class Solution:
    def countBits(self, num: int) -> List[int]:
       
        _1bits = []
        
        for i in range(num+1):
            count = 0
            while i > 0:
                if i % 2 == 1:
                    count += 1
                i >>= 1
            _1bits.append(count)
            
        return _1bits