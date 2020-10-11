# # Program to print table of a given number:

Num = int(input("Please enter a number for which table has to be printed: \n"))
Num1 = int(input("Please enter a number upto which you want a table: \n"))

print("The requested table is as follows: \n")

# for i in range(1, Num1+1):

#     print( Num * i)

N = 1
while N <= Num1:
    print(Num*N)
    N+=1