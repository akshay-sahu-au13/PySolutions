## https://practice.geeksforgeeks.org/problems/implement-queue-using-array/1/?category[]=Queue&company[]=Amazon&problemType=functional&page=1&sortBy=submissions&query=category[]Queuecompany[]AmazonproblemTypefunctionalpage1sortBysubmissions


class MyQueue:
    
    def __init__(self):
        self.Q = []
    
    def push(self, x):
         
         #add code here
         self.Q.append(x)
     
    def pop(self): 
        
        if len(self.Q)==0:
            return -1
         
        else:
            return (self.Q.pop(0))
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends