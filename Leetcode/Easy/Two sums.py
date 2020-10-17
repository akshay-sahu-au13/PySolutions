## https://leetcode.com/problems/two-sum/

 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            nums[x] = [nums[x],x]
            
        left = 0
        right = len(nums)-1
        nums.sort()
        
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1],nums[right][1]]
            
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            
            else:
                right -= 1
                
        return -1,-1
                