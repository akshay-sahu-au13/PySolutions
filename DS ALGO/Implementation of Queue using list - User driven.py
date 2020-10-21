## Question 2: Implement Queue using lists.

def enqueue(arr,x):

    arr.append(x)

def deque(arr):

    if len(arr) ==0:

        print("Nothing to deque.")

    else:

        arr.pop(0)



if __name__ == "__main__":
    arr = []
    while True:
        Op = int(input("Press 1 to Enqueue, 2 to Deque and 0 to exit: "))
        
        if Op == 1:
            x = int(input("Enter the number to Enqueue: "))
            enqueue(arr,x)
            print(f"Updated Queue: {arr}")

        elif Op == 2:
            deque(arr)
            print(f"Updated Queue: {arr}")  

        elif Op == 0:
            print("Thank you for trying this program, Bye!")
            break            

        else:
            print("Invalid Operation, please enter 1, 2 or 0")
