#User function Template for python3
## https://practice.geeksforgeeks.org/problems/middle-of-three2926/1#
class Solution:
    def middle(self,A,B,C):
        # R = sorted([A,B,C])
        # return R[1]
        
        if((A-B)*(A-C)<0) :
            return A
        elif((B-A)*(B-C)<0): 
            return B
        else:
            return C



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends