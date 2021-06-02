'''
Q-2 )Sort an array of 0s, 1s and 2s:(5 marks)
Given an array A[] consisting 0s, 1s and 2s. The task is to write a function that
sorts the given array. The functions should put all 0s first, then all 1s and all 2s in
last.
Examples:
Input: {0, 1, 2, 0, 1, 2}
Output: {0, 0, 1, 1, 2, 2}
Input: {0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1}
Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2}
'''





def sortArray(arr):
	left = 0
	right = len(arr) - 1
	mid = 0
	while mid <= right:
		if arr[mid] == 0:
			arr[left], arr[mid] = arr[mid], arr[left]
			left = left + 1
			mid = mid + 1
		elif arr[mid] == 1:
			mid = mid + 1
		else:
			arr[mid], arr[right] = arr[right], arr[mid]
			right = right - 1
	return arr
	


