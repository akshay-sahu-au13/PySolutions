

n = input("Enter a string: ")

dic = {}


for i in n:

    if i == " ":
        continue
    
    if i  not in dic:
        dic[i] = 1

    else:
       dic[i] += 1
      
print(dic)
