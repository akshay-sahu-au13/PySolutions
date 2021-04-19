num1 = int(input("Num1 = "))
num2 = int(input("Num2 = "))

for i in range(num1, num2+1):
    for j in range(2,i):
        if i%j != 0:
            continue
        else:
            break
    else:
        print(i)
