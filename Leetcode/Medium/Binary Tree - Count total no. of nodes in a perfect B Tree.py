## https://leetcode.com/problems/count-complete-tree-nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.Sum = 0
    def countNodes(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        self.Sum += 1
        
        self.countNodes(root.left)
        self.countNodes(root.right)
        
        return self.Sum
