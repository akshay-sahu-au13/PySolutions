## https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

### Using Queue ##
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        Q = []
        Q.append(root)
        Q.append(None)
        Final = []
        while len(Q) > 1:
            res = []
            while Q[0] != None:
                temp = Q.pop(0)
                res.append(temp.val)
                
                if temp.left:
                    Q.append(temp.left)

                if temp.right:
                    Q.append(temp.right)
                
            Final.append(res)
            Q.pop(0)
            Q.append(None)
            
        return Final
                