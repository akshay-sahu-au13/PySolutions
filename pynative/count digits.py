# Given a number count the total number of digits in a number
# For example, the number is 75869, so the output should be 5.

num = int(input("Enter the number: "))
digits = 0
while (num!=0):
    num //= 10
    digits += 1
print(digits)