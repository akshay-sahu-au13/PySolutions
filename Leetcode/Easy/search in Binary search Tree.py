## https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = None
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if root is None:
            return
        
        if root.val == val:
            self.res = root
        
        self.searchBST(root.left,val)
        
        self.searchBST(root.right,val)
        
        return self.res