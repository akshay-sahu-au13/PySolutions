## https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = bin(n)[::-1][:-2]
        reverse += "0"*(32-len(reverse))
        return int(reverse,2)
        
####### Another approach ######
## https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:

        rev = ""
        while n:
            
            if n % 2 == 1:
                rev += "1"
            else:
                rev += "0"
            
            n >>= 1
        
        rev += "0" * (32-len(rev))
        return int(rev,2)

### Another approach ###
class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        rev = 0
        while i < 31:
            bit = n & 1
            rev = rev | bit
            n >>= 1
            rev <<= 1
            i += 1
        return rev