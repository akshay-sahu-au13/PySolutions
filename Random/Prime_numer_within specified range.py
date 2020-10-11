# Python program to display all the prime numbers within a range

Start = int(input("Enter the starting number: "))
End = int(input("Enter the ending numner:"))

# Prime = [1,2]


for i in range(Start, End+1):

    # if i == 1 and i == 2:
    #     continue

    for j in range(2, i):

        if i % j == 0:
            break

    else:
        print(i)



        
            







