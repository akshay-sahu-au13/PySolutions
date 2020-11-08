## Selection Sort

def Selection_sort(ar):
    for i in range(len(ar)-2):
        min_i = i
        for j in range(i+1,len(ar)):
            if ar[j]<ar[min_i]:
                min_i = j
        ar[i],ar[min_i] = ar[min_i],ar[i]

    return ar

if __name__ == "__main__":
    print("Enter the array elements seperated by space: ")
    ar = list(map(int,input().split()))
    print(Selection_sort(ar))
