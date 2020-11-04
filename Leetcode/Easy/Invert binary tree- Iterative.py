## https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        
        queue = [root]
        
        while queue:
            temp = queue.pop(0)
            if temp is None:
                continue
            self.Swap(temp)
            queue.append(temp.left)
            queue.append(temp.right)
    
        return root
            
        
    def Swap(self,root):
 
        root.left,root.right = root.right,root.left
        