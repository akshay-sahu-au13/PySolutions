### https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## Brute force approach
        res = []
        for i in nums1:
            
            for j in nums2[nums2.index(i):]:
                
                if j > i:
                    res.append(j)
                    break
            else:
                res.append(-1)
        return res