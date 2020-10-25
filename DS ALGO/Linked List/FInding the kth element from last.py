## FInd the kth element from last

class Node:
    def __init__ (self, data  = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = Node()

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find_k_from_last(self,k,):
        first = org_head = self.head
        second = self.head
        count = 0
        while self.head:
            
            if count > k:
                second = second.next

            first = first.next
            count += 1
            self.head = self.head.next
        
        self.head = org_head

        print(f"\nThe kth element '{k}' from last is {second.data}")

    def display(self):
        temp = org_head = self.head
        if not self.head:
            print("Linked list is Empty")
            return
        while temp.next:
            print(f"{temp.data} --> ", end = "")
            temp = temp.next

        # self.head = org_head
if __name__ == "__main__":

    my_list = linked_list()
    my_list.push(4)
    my_list.push(5)
    my_list.push(3)
    my_list.push(7)
    my_list.push(8)
    my_list.push(43)
    my_list.push(9)
    my_list.display()
    my_list.find_k_from_last(4)
