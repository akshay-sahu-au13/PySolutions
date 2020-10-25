## https://leetcode.com/problems/binary-tree-level-order-traversal/

class Solution:

######### Using Recursion ######

     def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        def helper(Node_list, Res):
            Val = []
            Nodes = []
            if not Node_list:
                return Res
            
            for i in Node_list:
                Val.append(i.val)
                
                if i.left != None:
                    Nodes.append(i.left)
                
                if i.right != None:
                    Nodes.append(i.right)
                    
            Res.append(Val)
            return helper(Nodes, Res)

        Res = []
        if root == None:
            return Res
        
        return helper([root],Res)