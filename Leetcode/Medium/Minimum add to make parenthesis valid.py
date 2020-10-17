## https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        counter = 0
        for i in S:
            if not stack and i == ")":
                counter += 1
            
            elif i == "(" :
                stack.append(i)
                
            else:
                stack.pop()
                
        return counter + len(stack)