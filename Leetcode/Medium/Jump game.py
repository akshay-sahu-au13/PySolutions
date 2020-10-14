## https://leetcode.com/problems/jump-game/


class Solution:
    
         
    def canJump(self, nums: List[int]) -> bool:
        return self.ReachDesiredIndex(nums,len(nums)-1)
    def ReachDesiredIndex(self,nums,desiredIndex):
        # base case 
        if(desiredIndex == 0):
            return True
        
        # desired jumpLength = desiredIndex - i
        for i in range(desiredIndex-1, -1, -1):
            if(nums[i] >= desiredIndex - i):
                return self.ReachDesiredIndex(nums, i)
        
        return False