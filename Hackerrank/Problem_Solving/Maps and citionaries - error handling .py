# Enter your code here. Read input from STDIN. Print output to STDOUT
## https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
if __name__ == "__main__":
    phonebook = {}
    for i in range(int(input())):
        Pb = input().split()
        Name = Pb[0]
        Number = Pb[1]
        phonebook[Name] = Number
  
    while True:
        try:
            request = input()
            if request in phonebook:
                print(f"{request}={phonebook[request]}")
            else:
                print("Not found")
        except:        
            break
            
        
        
