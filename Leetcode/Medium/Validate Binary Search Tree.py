## https://leetcode.com/problems/validate-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.res = []
        
        if root is None:
            return True
        
        self.inorder(root)
        print(self.res)
        return sorted(set(self.res)) == self.res
        
    def inorder(self,root):
        if root is None:
            return

        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
    
        