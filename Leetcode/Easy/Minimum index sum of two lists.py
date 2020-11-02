### https://leetcode.com/problems/minimum-index-sum-of-two-lists

# class Solution:
#     def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
#         if not list1 and not list2:
#             return []
        
#         Op = {}
#         for i,j in enumerate(list1):
#             for k,l in enumerate(list2):
#                 if j == l:
                    
#                     if i+k not in Op:
#                         Op[i+k] = [j]
#                     else:
#                         Op[i+k].append(j)
#         # print(Op)
#         keys = []
#         for k1 in Op.keys():
#             keys.append(k1)
        
#         return Op[min(keys)] if len(Op)>1 else Op[k1]
            
##### Another good solution #####
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = dict(zip(list1, list(range(len(list1)))))
        result = []
        min_ind_sum = float("inf")
        for ind, restaurant in enumerate(list2):
            if restaurant in dict1.keys() and dict1[restaurant] + ind < min_ind_sum:
                min_ind_sum =  dict1[restaurant] + ind
                result = [restaurant]
            elif restaurant in dict1.keys() and dict1[restaurant] + ind == min_ind_sum:
                result.append(restaurant)
                
                
        return result
            
                    
                
            