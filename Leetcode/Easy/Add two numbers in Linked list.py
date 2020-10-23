## https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        while not l1 and not l2:
            return l1
        l = []
        r = []
        while l1:
            l.append(l1.val)
            l1 = l1.next
            
        while l2:
            r.append(l2.val)
            l2 = l2.next
            

        l = int("".join(list(map(str,l[::-1]))))
        r = int("".join(list(map(str,r[::-1]))))
        
        Res = str(l+r)[::-1]
        Res = list(map(int,list(Res)))
        
        temp = R = ListNode(0)
        
        for i in Res:
            new_node = ListNode(i)
            temp.next = new_node
            temp = temp.next
        
        return R.next
            
        
        
        