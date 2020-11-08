## https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if cloned is None:
            return
        res = [cloned]
        while res:
            
            clone = res.pop()
            
            if clone.val == target.val:
                return clone
            
            if clone.left:
                res.append(clone.left)
            
            if clone.right:
                res.append(clone.right)
            
            