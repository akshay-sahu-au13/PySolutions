## https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        stack = []
        
        for i in S:
            
            if not stack:
                
                stack.append(i)
                
            else:
                
                if stack[-1] == i:
                    stack.pop()
                    
                else:
                    stack.append(i)
                    
        return "".join(stack)
                    
                    
                