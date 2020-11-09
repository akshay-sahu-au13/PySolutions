## https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 1
        while i<len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i-1)
                i -= 1
            i += 1
            