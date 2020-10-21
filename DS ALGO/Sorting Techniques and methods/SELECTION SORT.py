################## SELECTION SORT ##################

def Selection_sort(A):
    
    for i in range(len(A)):

        min_idx = i

        for j in range(i+1,len(A)):

            if A[j] < A[min_idx]:

                min_idx = j

        A[i],A[min_idx] = A[min_idx],A[i]
        # print(A)  ## debug

    return A

B = [4,6,2,7,8,99,1,23,5,9,3]
print(B, "----->", end = " ")
print(Selection_sort(B))

