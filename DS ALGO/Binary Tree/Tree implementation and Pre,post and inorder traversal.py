## Implementing Binary Tree and Pre, post and Inorder Traversals

class Node(object):
     def __init__ (self,val = None):
         self.val = val
         self.left = None
         self.right = None

class Binary_Tree(object):
    def __init__(self,root):
        self.root = Node(root)
                                                  ## Tree ##
Tree = Binary_Tree(5)                    #             5
Tree.root.left = Node(2)                 #       2           3
Tree.root.right = Node(3)                #    7     8     9     1
Tree.root.left.left = Node(7)
Tree.root.left.right = Node(8)
Tree.root.right.left = Node(9)
Tree.root.right.right = Node(1)

## Preorder Traversal:

class Traversal:
    
    def preorder(self, root):

        if root is None:
            return None

        print(root.val, end = " - ")

        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):

        if root is None:
            return None

        self.postorder(root.left)
        self.postorder(root.right)

        print(root.val, end = " - ")

    def Inorder(self, root):

        if root is None:
            return None

        self.Inorder(root.left)
        print(root.val, end = " - ")
        self.Inorder(root.right)

        

Traverse = Traversal()
print("Pre order Traversal sequence: ", end = " ")
Traverse.preorder(Tree.root)
print()
print("Post order Traversal sequence: ",end = " ")
Traverse.postorder(Tree.root)
print()
print("In order Traversal sequence: ",end = " ")
Traverse.Inorder(Tree.root)


