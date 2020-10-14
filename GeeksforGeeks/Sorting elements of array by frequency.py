### https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0

if __name__ == "__main__":
    
    for i in range(int(input())):
        
        d = {}
        N = int(input())
        A = list(map(int,input().split()))
        
        for i in A:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        for j in sorted(d, key = d.get, reverse = True):
            for i in range(d[j]):
                print(j, end = " ")
        print()
        