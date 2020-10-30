## https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        node_val = []
        res = tmp_res = ListNode()
        while head:
            node_val.append(head.val)
            head = head.next
        for v in node_val[:m - 1]:
            tmp_res.next = ListNode(v)
            tmp_res = tmp_res.next
        for i in range(n - 1, m - 2, -1):
            tmp_res.next = ListNode(node_val[i])
            tmp_res = tmp_res.next
        for v in node_val[n:]:
            tmp_res.next = ListNode(v)
            tmp_res = tmp_res.next
        return res.next
        