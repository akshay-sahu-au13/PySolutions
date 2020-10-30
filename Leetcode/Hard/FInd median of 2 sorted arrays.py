## https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return nums1/2
        
        nums = nums1+nums2
        nums.sort()
        l = len(nums)
        
        if l%2 ==0:
            return (nums[int(l/2)]+nums[int((l/2)-1)])/2
        else:
            return float(nums[l//2])
            
        