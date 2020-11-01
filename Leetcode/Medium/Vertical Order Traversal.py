## https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return []
       
        q = []
        node_list = []
        q.append([root, 0, 0])
        while q:
            node, col, row = q.pop(0)
            node_list.append((col, row, node.val))
            if node.left:
                q.append([node.left, col - 1, row + 1])
            if node.right:
                q.append([node.right, col + 1, row + 1])
        node_list.sort()
        ans = {}
        for col, row, val in node_list:
            if col not in ans:
                ans[col] = []
            ans[col].append(val)
            
        return ([ans[x] for x in ans])