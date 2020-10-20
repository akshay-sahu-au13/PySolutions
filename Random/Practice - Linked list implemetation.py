
## Linked List implementation  - Append, delete, length, display methods: 

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elements = []
        current = self.head
        while current.next != None:
            current = current.next
            elements.append(current.data)
        print(elements) 

    def get(self,index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return
        current = self.head
        i = 0
        while current.next != None:
            current = current.next
            if i == index:
                print(f"Value at index {index} is {current.data}")
                return current.data
            i += 1

    def Delete(self, index):
        if self.length() ==0:
            print("ERROR: Linked list is empty, Nothing to delete!")
            return None
        elif index > self.length():
            print("ERROR: Index out of Range")
            return None
        else:
            cur = self.head
            i = 0
            while True:
                lst_node = cur
                cur = cur.next
                if i == index:
                    lst_node.next = cur.next
                    print(f"{cur.data} is deleted from index {index}")
                    return
                i += 1

### Execution ###

my_list = Linkedlist()
my_list.display()
my_list.append(29)
my_list.display()
my_list.length()
my_list.append(77)
my_list.display()
my_list.append(123)
my_list.display()
print("The length of the linked list is: ",my_list  .length())
my_list.get(1)
my_list.get(3)
print(my_list.get(1))
my_list.Delete(6)
my_list.Delete(1)
my_list.display()