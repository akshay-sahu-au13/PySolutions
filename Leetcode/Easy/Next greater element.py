##### https://leetcode.com/problems/next-greater-element-i/

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         ## Brute force approach
#         res = []
#         for i in nums1:
            
#             for j in nums2[nums2.index(i):]:
                
#                 if j > i:
#                     res.append(j)
#                     break
#             else:
#                 res.append(-1)
#         return res
                
#         ## Using Stacks
        
# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         next_greater = {}
        
#         stack_end = -1
#         for n in nums2:               
#             while stack_end >=0 and n > nums2[stack_end]:
#                 next_greater[nums2[stack_end]] = n
#                 stack_end -= 1
                    
#             stack_end += 1
#             nums2[stack_end] = n           
            
#         while stack_end >= 0:    
#             next_greater[nums2[stack_end]] = -1
#             stack_end -= 1
            
#         return [next_greater[n] for n in nums1]

###### Another solution #####

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {} # mapping from element to greater 
        stack = [] # non-increasing mono-stack
        for x in nums2: 
            while stack and stack[-1] < x: mp[stack.pop()] = x
            stack.append(x)
        return [mp.get(x, -1) for x in nums1]  #D.get(k[, x])--->Returns D[k] if k is a key                                                  #in D; otherwise, returns x (or None, if x is not given)
    #(Refer:https://www.oreilly.com/library/view/python-in-a/0596100469/ch04s08.html)
        