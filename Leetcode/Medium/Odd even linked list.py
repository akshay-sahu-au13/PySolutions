## https://leetcode.com/problems/odd-even-linked-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        
        if head == None or head.next == None :
            return head
        
        Odd_head = head
        Even_head = head.next
        
        odd_temp = head
        even_temp = head.next
        
        while odd_temp.next and even_temp.next:
            
            if Even_head.next == None:
                return Odd_head
                break
                
            odd_temp.next = even_temp.next
            odd_temp = odd_temp.next
            
            even_temp.next = odd_temp.next
            even_temp = even_temp.next
            
        odd_temp.next = Even_head
        
        return Odd_head
    