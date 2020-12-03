## https://leetcode.com/problems/number-of-1-bits/

class Solution:
	def hammingWeight(self, n: int) -> int:
		return bin(n).count("1")

####### Another approach ########

class Solution:
    def hammingWeight(self, n: int) -> int:
        bitcount = 0
        while n > 0:
            if n % 2 == 1:
                bitcount += 1
            n >>= 1
        return bitcount