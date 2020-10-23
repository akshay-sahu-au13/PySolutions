## https://leetcode.com/problems/intersection-of-two-linked-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
            
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        A = headA
        D = {}
        
        while A:
            
            D[A] = 1
            A = A.next 
            
        B = headB
        
        while B:
            
            if B in D:
                return B
            else:
                B = B.next 
            
        return 