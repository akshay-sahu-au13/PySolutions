## Practice of Tree Traversals

class TreeNode(object):
    def __init__(self,val = None,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):
    def __init__ (self,root = None):
        self.root = TreeNode(root)

    def TreeVisualizer(self,root):  ## Works only upto 3 level with perfect Tree
        print(f"""
                                        {root.val}
                                {root.left.val}              {root.right.val}
                            {root.left.left.val}      {root.left.right.val}      {root.right.left.val}      {root.right.right.val}
                """)

    def StackPreorder(self,root):
        stack = []
        if root is None:
            return
        stack.append(root)
        while stack:
            temp = stack.pop()
            print(temp.val,end = " - ")
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)

    def StackPostorder(self,root):   ## Using 1 stack
        stack = []
        if root is None:
            return
        
        while True:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()
            if root.right and stack and root.right == stack[-1]:
                stack.pop()
                stack.append(root)
                root = root.right
            else:
                print(root.val,end = " - ")
                root = None
            if len(stack) <= 0:
                break
    
    def Stack_Inorder(self,root):
        if root is None:
            return
        stack = []

        while True:
            if root:
                stack.append(root)
                root = root.left

            else:
                if not stack:
                    break
                temp = stack.pop()
                print(temp.val, end = " - ")
                root = temp.right



T = BinaryTree(5)
T.root.left = TreeNode(3)
T.root.right = TreeNode(6)
T.root.left.left = TreeNode(31)
T.root.right.left = TreeNode(1)
T.root.left.right = TreeNode(13)
T.root.right.right = TreeNode(16)
T.TreeVisualizer(T.root)
T.StackPreorder(T.root)
print()
T.StackPostorder(T.root)
print()
T.Stack_Inorder(T.root)