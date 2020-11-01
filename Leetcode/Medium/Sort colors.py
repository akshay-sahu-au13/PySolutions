# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
        # """
        ### USING BUBBLE SORT ###
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] >= nums[j]:
#                     nums[i],nums[j]=nums[j],nums[i]
                    
#         return nums
                    
        #### USING SELECTION SORT ####
        # for i in range(len(nums)):
        #     minidx = i
        #     for j in range(i+1,len(nums)):
        #         if nums[j] < nums[minidx]:
        #             minidx = j
        #     nums[i],nums[minidx] = nums[minidx],nums[i]
        
 ############## ANOTHER SOLUTION with O(N) time complexity and O(1) Space

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         zero_pointer = 0
#         two_pointer=len(nums)-1
#         i=0
#         while(i < len(nums) and zero_pointer < two_pointer):
#             if nums[i]==0 and i > zero_pointer:
#                 nums[zero_pointer],nums[i]=nums[i], nums[zero_pointer]
#                 zero_pointer+=1
#                 continue
#             elif nums[i]==2 and i < two_pointer:
#                 nums[two_pointer],nums[i]=nums[i],nums[two_pointer]
#                 two_pointer-=1
#                 continue
                
#             else:
#                 i+=1
              
    #### ANother method from TA session ####
        red,white,blue = 0,1,2
        redInd,blueInd = 0,len(nums)-1
        
        i = 0
        while i <= blueInd:
            if nums[i] == 2:
                nums[i],nums[blueInd] = nums[blueInd],nums[i]
                blueInd -= 1
            elif nums[i] == 0:
                nums[i],nums[redInd] = nums[redInd],nums[i]
                redInd += 1
                i+=1
            else:
                i+=1
                