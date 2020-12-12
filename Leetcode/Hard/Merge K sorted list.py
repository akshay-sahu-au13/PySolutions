"""
You are given an array of k linked-lists lists , each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
1->4->5,
1->3->4,
2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
•
•
•
• k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
• lists[i] is sorted in ascending order.
• The sum of lists[i].length won't exceed 10^4 .
"""
class Node:
    def __init__(self,val) -> None:
        self.data = val
        self.next = None

def addNodeToTailOfLL(head,x):
    if head == None:
        return Node(x)
    else:
        new_Node = Node(x)
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = new_Node

        return head

def printLL(head):
    temp = head
    while temp != None:
        print(temp.data, end=" ")
        temp = temp.next



import heapq

class Solution2:
    def mergeKLists(self, lists):

        min_heap, pointer = [], {}

        for i, list_node in enumerate(lists):
            if list_node:  
                pointer[i] = list_node
                heapq.heappush(min_heap, (list_node.data, i))

        if not min_heap:
            return None

        header = cur = None
        while(min_heap):
            _, list_index = heapq.heappop(min_heap)
            node = pointer[list_index]
            if node.next:
                pointer[list_index] = node.next
                heapq.heappush(min_heap, (node.next.data, list_index))

            if not header: 
                header = cur = node
            else:
                cur.next = node
                cur = cur.next
        return header

if __name__ == '__main__':
    print()

    head = None
    head = addNodeToTailOfLL(head,1)
    head = addNodeToTailOfLL(head,4)
    head = addNodeToTailOfLL(head,5)

    head1 = None
    head1 = addNodeToTailOfLL(head1,1)
    head1 = addNodeToTailOfLL(head1,3)
    head1 = addNodeToTailOfLL(head1,4)

    head2 = None
    head2 = addNodeToTailOfLL(head2,2)
    head2 = addNodeToTailOfLL(head2,6)

    print("First linked list is: ")
    printLL(head)
    print()
    print()
    print("Second linked list is:")
    printLL(head1)
    print()
    print()
    print("Third linked list is:")
    printLL(head2)
    print()
    print()

    list1 = []
    
    list1.append(head)
    list1.append(head1)
    list1.append(head2)

    secondIns = Solution2()

    mergedLL = secondIns.mergeKLists(list1)

    print("After merging the list of LL, new LL is: ")
    printLL(mergedLL)
    print()

    print()
    print("################################################################")
    print()