### https://leetcode.com/problems/sum-of-left-leaves/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.Sum = 0
        
    def isleaf(self,root):
        if root is None:
            return False 
        if root.left is None and root.right is None:
            return True
        return False
    
    def solve(self,root):
        if root is None:
            return 0
        
        if self.isleaf(root.left):
            self.Sum += root.left.val
            
        self.solve(root.left)
        self.solve(root.right)
        
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        self.solve(root)
        return self.Sum
    
        
        