## Implementing Binary Tree and Pre-Order, post-order, In-order and Level-Order Traversals

class Node(object):
     def __init__ (self,val):
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

        
    def Level_order(self,root):
        if root is None:
            return
        Q = []
        Q.append(root)
        Final = []

        while len(Q)>=1:
            for i in Q:
                temp = Q.pop(0)
                print(temp.val, end = " - ")
                if temp.left:
                    Q.append(temp.left)
                if temp.right:
                    Q.append(temp.right)
        
        # print(*Final)
            
            
if __name__ == "__main__":
    Traverse = Traversal()
    print("Pre order Traversal sequence: ", end = " ")
    Traverse.preorder(Tree.root)
    print()
    print("Post order Traversal sequence: ",end = " ")
    Traverse.postorder(Tree.root)
    print()
    print("In order Traversal sequence: ",end = " ")
    Traverse.Inorder(Tree.root)
    print()
    print("Level Order Traversal sequence: ",end = " ")
    Traverse.Level_order(Tree.root)


