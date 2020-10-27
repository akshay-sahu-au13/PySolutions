## https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
#         nums1 = nums[:n]
#         nums2 = nums[n:]
#         res= []
        
#         for i in range(len(nums1)):
            
#             res.append(nums1[i])
#             res.append(nums2[i])
            
#         return res
        res = []
        for i in range(len(nums)//2):
            res.append(nums[i])
            res.append(nums[i+n])
            
        return res