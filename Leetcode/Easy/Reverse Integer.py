## https://leetcode.com/problems/reverse-integer/submissions/
class Solution:
    def reverse(self, x: int) -> int:

        if x+1 > 0:
            a = int(str(x)[::-1])
            if a > (2**31) -1:
                return 0
            else:
                return a
        else:
            b = 0 - int(str(x)[1:][::-1])
            if b < -(2**31) :
                return 0
            else:
                return b