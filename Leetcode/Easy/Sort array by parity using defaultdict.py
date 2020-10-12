### https://leetcode.com/problems/sort-array-by-parity-ii/submissions/


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:

      # """
      # Dictionaries are a convenient way to store data for later retrieval by name (key).
      # A defaultdict works exactly like a normal dict, but it is initialized with a unction (“default factory”)
      # f that takes no arguments and provides the default value for a nonexistent key. A defaultdict will never raise a KeyError.
########Refer : https://www.geeksforgeeks.org/defaultdict-in-python/ ############
        d = defaultdict(list)
        
        for i in A:
            if i%2 == 0:
                d["Even"].append(i)
            else:
                d["odd"].append(i)
                
        for i in range(len(A)):
            if i%2 == 0:
                A[i] = d["Even"].pop()
            else:
                A[i] = d["odd"].pop()
                
        return A
                
                
        
            
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        