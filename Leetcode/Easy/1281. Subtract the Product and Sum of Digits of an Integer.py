## https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        
        N = list(map(int,list(str(n))))
        # print(N)
        Product = 1
        Sum = 0
        for i in N:
            Product *= i
            Sum += i
        return Product - Sum

        
        
            
            
            
        
        
        
        