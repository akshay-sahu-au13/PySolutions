## https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    
        if root is None:
            return True
        
        return self.Validate(root, None, None)
    
    def Validate(self,root,min,max):
        
        if root is None:
            return True
        
        if (min != None and min >= root.val) or (max != None and max <= root.val):
            return False
            
        return self.Validate(root.left,min,root.val) and self.Validate(root.right,root.val,max)