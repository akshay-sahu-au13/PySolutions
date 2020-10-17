### https://leetcode.com/problems/contains-duplicate/submissions/ ###

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    ##### Method 1 #####
        
        # return not len(nums) == len(list(set(nums)))
    
    ##### Method 2 #####
        
        d = {}
        
        for i in nums:
            
            if i in d:
                return True
            else:
                d[i] = True  ## Can take anything as a value here
                
        return False
        
         