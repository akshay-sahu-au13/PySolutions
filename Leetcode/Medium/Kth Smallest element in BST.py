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
       
######## ANOTHER APPROACH WITH BETTER RUNTIME ######

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans, stack = [], [(root, False)]
        while stack and len(ans)<k:
            node, visited = stack.pop()
            if node:
                if visited:
                    ans.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return ans[-1]