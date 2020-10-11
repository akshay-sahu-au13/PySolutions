n = int(input("How many entries do you want in the list?"))

list = []

for i in range(0, n):

    num = int(input("Keep entering the number is the list: "))
    list = list.append(num)

max = 0

for j in list:

    if max < j:
        
        max = j

print("The maximun number in list: ", list, "is", max)
