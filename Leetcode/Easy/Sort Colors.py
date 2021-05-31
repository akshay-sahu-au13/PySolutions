# https://leetcode.com/problems/sort-colors/submissions/
# Given an array nums with n objects colored red, white, or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order red,
# white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
# respectively.
# You must solve this problem without using the library's sort function.
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


def sortColors(nums):
    
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    for i in range(n):
        for j in range(0, n-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


if __name__ == "__main__" :

    nums = [2,0,2,1,1,0]
    ans = sortColors(nums)
    print(ans)