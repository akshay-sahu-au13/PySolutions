# Q1. https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = (x+1)//2
        
        while left<=right:
            
            mid = (left+right)//2
            
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid -1
            else:
                # if mid*mid < x and 
                left = mid +1
                
        return left-1