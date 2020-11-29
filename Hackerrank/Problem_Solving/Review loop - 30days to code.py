# Enter your code here. Read input from STDIN. Print output to STDOUT
## https://www.hackerrank.com/challenges/30-review-loop
if __name__ == "__main__":
    
    n = int(input())
    for i in range(n):
        odd = ""
        even = ""
        strng = input()
        for j in range(len(strng)):
            if j%2 == 1:
                odd += strng[j]
            else:
                even += strng[j]
                
        print(f"{even} {odd}")
        