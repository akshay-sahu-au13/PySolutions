## https://leetcode.com/problems/single-number

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ### Method 1 ###
        nums.sort()
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[i]
        
        ### Method 2 ### 
        
class Solution:
    def singleNumber(self, nums: List[int]) -> int:        
        bit = 0
        for i in range(len(nums)):
            bit  = bit ^ nums[i]
            
        return bit
                                    
        
            