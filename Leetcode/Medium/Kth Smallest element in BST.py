# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__ (self):
        self.temp  = []
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return 
        self.inorder(root)
        return self.temp[k-1]
        
    def inorder(self,root):
        if root is None:
            return
        
        self.inorder(root.left)
        self.temp.append(root.val)
        self.inorder(root.right)
       
        