# Enter your code here. Read input from STDIN. Print output to STDOUT
## https://www.hackerrank.com/challenges/maximum-element/problem
stack = []
maxStack = [0]
for i in range(int(input())): #N
    query = input().split()
    if len(query)>1:
        Op = 1
        x = int(query[1])
        stack.append(x)
        if maxStack[-1] <= x:
            maxStack.append(x)
            
    else:
        Op = int(query[0])
        
        if Op == 2:
            if stack.pop() == maxStack[-1]:
                maxStack.pop()
        else:
            print(maxStack[-1])  