## Question 1: Implement Queue using stacks

def Enqueue(x,stack1,stack2):

    stack1.append(x)

def Deque(stack1,stack2):

    if not stack1 and not stack2:
        print("Cannot deque from an empty list")

    elif len(stack2) ==0:

        while stack1:

            stack2.append(stack1.pop())

        return stack2.pop()

    else:

        return stack2.pop()


if __name__ == "__main__":
    stack1 = []
    stack2 = []
    q = []

    while True:
        Op = int(input("Enter 1 for Enqueue, 2 for Deque and 0 to EXIT: "))
        if Op == 1:
            x = int(input("Enter a value to be Enqueued: "))
            Enqueue(x,stack1,stack2)
            print(f"{x} is Enqueued to the existing Queue.")
            q.append(x)
            print(f"Updated Queue is : {q}")
        elif Op == 2:
            print(f"{Deque(stack1,stack2)} is Dequed from the Queue")
            q.pop(0)
            print(f"Updated Queue is : {q}")
        elif Op == 0:
            print(f"Thanks for testing the Queue program. \nFinal Queue is {q}")
            break
        else:
            print("Invalid Operation!!!")

