###### INSERTION SORT -- Practice ######

def InsertionSort(arr):

    for i in range(1,len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            arr[j] = key
            j -= 1
        arr[j+1] = key  

if __name__ == "__main__":
    
    arr = list(map(int,input("Enter the array elements separated by space: \n").split()))
    # arr = [2,5,1,33,4,23,9]
    print("The given array is: ",arr)
    
    InsertionSort(arr)
    print("Sorted Array is: ",arr)
    