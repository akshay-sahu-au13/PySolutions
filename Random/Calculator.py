# Calculator

print(
        """
        Hey, this is an Awesome calculator...
        These are the operations supported by it.
        1 for addition
        2 for Multiplication
        3 for Division
        4 for Substraction
        5 for power(x,y)
        6 for exit
        """
    )
while True:

    X = float(input("Please enter the value of X: "))
    Y = float(input("Please enter the value of Y: "))
    Opr = int(input("Kindly enter the operation code - - - "))
    
    if Opr == 6:
        print("Thank you for using CalC, Come again tomorrow!")
        break
    Result = 0
    if Opr == 1:
        Result = (X+Y)
    elif Opr == 2:
        Result =(X*Y)
    elif Opr == 3:
        Result =(X/Y)
    elif Opr == 4:
        Result =(X-Y)
    elif Opr == 5:
        Result =(X**Y)
    else:
        print("This is not a valid operation!")
        continue
    print("Your result is : ", Result)