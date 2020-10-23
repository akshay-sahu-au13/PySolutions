## https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.Sum = 0
        self.isleft = False
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        if root ==  None:
            return 0
        
        if root.left is None and root.right is None and self.isleft is True :
            
            self.Sum += root.val
            return
        
        self.isleft = True
        
        self.sumOfLeftLeaves(root.left)
        
        self.isleft = False
        
        self.sumOfLeftLeaves(root.right)
      
        return self.Sum
        