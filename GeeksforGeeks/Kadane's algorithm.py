#User function Template for python3
## https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1#
##Complete this function
def maxSubArraySum(a,size):
    ##Your code here
    max1 = a[0]
    maxfinal = a[0]
    
    for i in range(1,size):
        max1 = max(a[i],max1+a[i])
        maxfinal = max(max1,maxfinal)
    
    return maxfinal


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            print(maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends