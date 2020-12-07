

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new_node = Node(data)
        if head is None:
            head = new_node
        else:
            temp = head
            while temp.next:
                
                temp = temp.next
            temp.next = new_node
        return head
 ## https://www.hackerrank.com/challenges/30-linked-list/problem   

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  