##https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.lst = []
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return 
        
        self.postorderTraversal(root.left)
        self.postorderTraversal(root.right)
        self.lst.append(root.val)
        
        return self.lst
        
    