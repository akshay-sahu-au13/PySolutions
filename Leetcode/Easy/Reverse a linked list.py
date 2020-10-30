## https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return
        
#         prev = None
#         cur = head
#         temp = head.next
        
#         while cur:
#             cur.next = prev
#             prev = cur
#             cur = temp
#             if cur is not None:
#                 temp = temp.next
#         return prev
## Another solution 
        prev = None
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev