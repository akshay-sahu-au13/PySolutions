### Q: Write a program to insert, delete at beginning, end, middle of a linked list.
class node:

    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linked_list:

    def __init__(self):

        self.head = node()

    def insert_at_end(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        print(f"Element {new_node.data} is added at the end")
        cur.next = new_node

    def insert_at_start(self,data):
        cur = self.head
        temp = cur.next
        new_node = node(data)
        cur.next = new_node
        new_node.next = temp
        print(f"Element {new_node.data} is added at the start")
    
    def insert_at_index(self,index,data):

        if self.length() < index:
            print("ERROR! List index out of range!")
            return None
        cur = self.head
        new_node = node(data)
        i = 0
        while True:
            
            temp = cur.next
            if i == index:
                cur.next = new_node
                new_node.next = temp
                print(f"Element {new_node.data} is added at the index position {index}")
                return
            cur = cur.next
            i += 1

    def delete_from_index(self,index):
        if self.length() == 0:
            print("ERROR! List is Already Empty")
            return None
        elif index >= self.length():
            print("ERROR! List index out of range!")
            return None

        else:
            cur = self.head
            # cur = cur.next
            i = 0
            while True:
                lst_node = cur
                cur = cur.next
                if i == index:
                    print(f"Element {cur.data} is removed from index {index}")
                    lst_node.next = cur.next
                    return
                i +=1

    def delete_from_start(self):
        cur = self.head
        print(f"Element {cur.next.data} is removed from start.")
        cur.next = cur.next.next
        return

    def delete_from_last(self):
        cur = self.head

        while cur.next.next != None:
            cur = cur.next
        print(f"Element {cur.next.data} is removed from end")
        cur.next = None
        return
    
    def length(self):
        total = 0
        cur = self.head
        while cur.next != None:
            total+=1
            cur = cur.next
        # print(f"Length of the current list is {total}")
        return total

    def display(self):
        res= []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            res.append(cur.data)
            
        print(f"Current linked list is {res}")




if __name__ == "__main__":

    my_list = Linked_list()

    print("              Welcome! Please try you hands on the linked list program: ")
    def Menu():
        print("""
                            -------------- M E N U --------------
                            Press 1 to Add an element at start
                            Press 2 to Add an element at last
                            Press 3 to Add an element at an index position
                            Press 4 to Delete an element from Head
                            Press 5 to Delete an element from an index
                            Press 6 to Delete an element from Tail

                            Type Len to check the length of the List
                            Type Display to see the current list
                            Type MENU to see the Menu at any point of time
                            Type Exit or Quit to end the program!

                            
                        """)
    Menu()

    while True:

        Op = input("====>")

        if Op == "1":
            my_list.insert_at_start(int(input("Enter the Number to be added: ")))
        
        elif Op == "2":
            my_list.insert_at_end(int(input("Enter the Number to be added: ")))
        
        elif Op == "3":
            my_list.insert_at_index(int(input("Enter the index value: ")), int(input("Enter the Number to be added: ")))

        elif Op == "4":
            my_list.delete_from_start()

        elif Op == "5":
            my_list.delete_from_index((int(input("Enter the index value: "))))

        elif Op == "6":
            my_list.delete_from_last()

        elif Op.lower() == "len":
            print("The length of current list is: ",my_list.length())
        
        elif Op.lower() == "display":
            my_list.display()
        
        elif Op.lower() == "menu":
            Menu()

        elif Op.lower() == "exit" or Op.lower() == "quit":
            print("Thank you for checking this program. Bye!")
            break
        else:
            print("Invalid Operation! Please check the MENU and enter an appropriate input/command.")
