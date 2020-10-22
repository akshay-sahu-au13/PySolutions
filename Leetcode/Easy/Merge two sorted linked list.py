#https://leetcode.com/problems/merge-two-sorted-lists
# 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return
        res = []
        
        while l1 and l2:  ## comparing and adding the smaller value to the list
            
            if l1.val > l2.val:
                res.append(l2.val)
                l2 = l2.next  
            else:
                res.append(l1.val)
                l1 = l1.next
             
        while l1:   ## Adding the remaining value of LL 1 if any
            res.append(l1.val)
            l1 = l1.next
            
        while l2:   ## Adding the remaining value of LL2 if any
            res.append(l2.val)
            l2 = l2.next
        
        L = temp = ListNode()
        
        for x in res:  ## Creating a linked list out of res list
            new_node = ListNode(x)
            temp.next = new_node
            temp = temp.next
        
        return L.next