## https://leetcode.com/problems/palindrome-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        res = []
        if not head:
            return True
        
        while head:
            res.append(head.val)
            head = head.next
        print(res,res[::-1])

        return res == res[::-1]
            