Num = int(input("Enter a number: "))

Q = int(Num/10)

D = 1

while Q != 0:

    Q = Q//10
    D = D+1
    
print("Total digits in given number is: ", D)
