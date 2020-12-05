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

### Memoization solution ###


class Solution:
    def countBits(self, num: int) -> List[int]:
        if num == 0:
            return [0]
        if num == 1:
            return [0,1]
        result = [0, 1]
        for n in range(2,num+1):
            if n % 2 == 0:
                result.append(result[int(n/2)])
            else:
                result.append(result[int(n/2)]+1)
        return result