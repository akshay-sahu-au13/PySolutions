## https://www.hackerrank.com/challenges/30-binary-trees/problem

import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        q = [root]
        res = []
        while q:
            a = q.pop(0)
            if a.left:
                q.append(a.left)
            if a.right:
                q.append(a.right)
            
            res.append(a.data)
        print(*res)
        

T=int(input())