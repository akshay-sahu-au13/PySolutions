  
def findSingle( ar, n):
     
    res = ar[0]
    for i in range(1,n):
        res = res ^ ar[i]
     
    return res
 

ar = [ 3, 5, 2, 4, 5, 3, 4]
print ("Element occurring once is", findSingle(ar, len(ar)))