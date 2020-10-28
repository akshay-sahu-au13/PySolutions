class TreeNode(object):
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self,root = None):
        self.root = TreeNode(root)
        self.stack = []
        self.stack2 = []

    def TreeVisualizer(self,root):  ## Works only upto 3 level with perfect Tree
        print(f"""
                                        {root.val}
                                {root.left.val}              {root.right.val}
                            {root.left.left.val}      {root.left.right.val}      {root.right.left.val}      {root.right.right.val}
                        
                """)


    def stack_preorder(self,root):
        
        if root:
            self.stack.append(root)
        else:
            return

        while self.stack:
            temp = self.stack.pop()
            print(temp.val, end = " - ")

            if temp.right:
                self.stack.append(temp.right)
            if temp.left:
                self.stack.append(temp.left)
        
        return "end"

    def stack_postorder(self,root):  ## Using 2 stacks
        # self.stack2 = []
        if root:
            self.stack.append(root)
        else:
            return self.stack
        while self.stack:
            temp = self.stack.pop()
            self.stack2.append(temp.val)

            if temp.left:
                self.stack.append(temp.left)

            if temp.right:
                self.stack.append(temp.right)
        for i in self.stack2[::-1]:
            print(i, end = " - ")
        return "end"

    def stack_Inorder(self,root):
        if root is None:
            return

        while True:
            
            if root != None:
                self.stack.append(root)
                root = root.left
            
            else:
                if not self.stack:
                    break
                temp = self.stack.pop()
                print(temp.val, end = " - ")
                root = temp.right

        return "end"
Tree = BinaryTree(5)
Tree.root.left = TreeNode(55)
Tree.root.right = TreeNode(3)
Tree.root.left.left = TreeNode(12)
Tree.root.left.right = TreeNode(14)
Tree.root.right.left = TreeNode(47)
Tree.root.right.right = TreeNode(34)
print("Pre-order Traversal: ",end = " ")
print(Tree.stack_preorder(Tree.root))
Tree.TreeVisualizer(Tree.root)
print("Post-order Traversal: ",end = " ")
print(Tree.stack_postorder(Tree.root))
print("In-order Traversal: ",end = " ")
print(Tree.stack_Inorder(Tree.root))

