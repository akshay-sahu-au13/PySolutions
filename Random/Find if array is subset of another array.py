# Find whether an array is subset of another array:(5 marks)
# Examples:
# Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1}
# Output: arr2[] is a subset of arr1[]
# Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4}
# Output: arr2[] is a subset of arr1[]
# Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3}
# Output: arr2[] is not a subset of arr1[]


def findSubsetArr(arr1, arr2):
    count = 0
    temp = False
    for i in range(0, len(arr1)):
        for j in range(0, len(arr2)):
            if arr1[i] == arr2[j]:
                count = count + 1
            if count == len(arr2):
                temp = True
    if temp == True:
        print("arr2[] is subset of arr1[]")
    else:
        print("arr2[] is not a subset of arr1[]")



if __name__ == "__main__":
	
	# arr1 = [11, 1, 13, 21, 3, 7]
	# arr2 = [11, 3, 7, 1]

	arr1 = [10, 5, 2, 23, 19]
	arr2 = [19, 5, 3]

	findSubsetArr(arr1, arr2)