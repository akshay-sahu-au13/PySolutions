##https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.next if  fast.next else slow