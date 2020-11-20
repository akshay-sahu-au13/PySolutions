
## https://leetcode.com/problems/roman-to-integer/
class Solution:
    def romanToInt(self, s: str) -> int:
        Val = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        total = 0
        prev = 0
        cur = 0

        for i in s:

            cur = Val[i]
            if prev < cur:
                total = total + cur - 2*prev
            else:
                total += cur
            prev = cur
        
        return total