### https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        

#         first = -1
#         last = -1
#          ## For first position
#         left = 0
#         right = len(nums)-1
#         while left <= right: 
#             mid = (left+right)//2
            
#             if nums[mid] == target:
#                 first = mid
#                 right = mid-1
#             elif nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid -1
                
#         # for last position        
#         left = 0
#         right = len(nums)-1            
#         while left<=right:
#             mid = (left+right)//2
            
#             if nums[mid] == target:
#                 last = mid
#                 left = mid+1
#             elif nums[mid] < target:
#                 left = mid+1
#             else:
#                 right = mid -1
        
#         return(first,last)

###########################PRACTICE#########################
#         first = -1
#         last = -1
#         l = 0
#         r = len(nums)-1
        
#         while l <= r:
#             mid = (l+r)/2
            
#             if nums[mid] == target:
#                 return mid
#                 r = mid-1
            
#             if nums[mid] < target:
#                 l = mid+ 1
            
#             else:
#                 r = mid -1
                
        
        
        
# ## Using for loop
# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:      
#         l = -1
#         r = -1
#         for i in range(len(nums)):
#             if nums[i]==target:
#                 l = i
#                 break
#         else:
#             return [l,r]
#         for j in range(len(nums)-1, -1,-1):
#             if nums[j] == target:
#                 r = j
#                 break
            
#         return [l,r]
    
        start = 0; 
        end = len(nums)-1
        
        while start <= end:
            mid = (start+end) // 2
            
            if nums[start] == nums[end] == target:
                return [start, end]
            
            if nums[mid] < target:
                start = mid+1
                
            elif nums[mid] > target:
                end = mid-1
            else:
                if nums[start] != target: start += 1
                if nums[end] != target: end -= 1
        return [-1,-1]

        
                
        