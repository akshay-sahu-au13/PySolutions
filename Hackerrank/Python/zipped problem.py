# Enter your code here. Read input from STDIN. Print output to STDOUT
##https://www.hackerrank.com/challenges/zipped/problem

Scores = []
n, x = map(int, input().split())
for i in range(x):
    Marks = map(float, input().split())
    Scores.append(Marks)
for i in zip(*Scores): 
    print( sum(i)/len(i) )
