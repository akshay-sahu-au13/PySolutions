################# BUBBLE SORT ##################

A = [3,5,2,6,7,1,88,51,4,3,21,8]
def Bubblesort(A):
    for i in range(len(A)):

        for j in range(len(A)-1-i):

            if A[j] > A[j+1]:

                A[j],A[j+1] = A[j+1],A[j]
        
        # print(A)   ## Debug

    return A

print(Bubblesort(A))

