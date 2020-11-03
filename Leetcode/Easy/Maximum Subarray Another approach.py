## https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsofar = 0
        a=[]
        maxending = 0
        for i in range(len(nums)):
            maxending = maxending + nums[i]
            if maxending < 0 :
                a.append(maxending)
                maxending = 0
            elif maxsofar< maxending:
                maxsofar = maxending
        if maxsofar == 0 and a != []:
            return max(nums)
        else:
            return maxsofar
            
        