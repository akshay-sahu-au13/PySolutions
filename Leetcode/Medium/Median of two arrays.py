## https://leetcode.com/problems/median-of-two-sorted-arrays/

def findMedianSortedArrays(nums1, nums2):
    nums = sorted((nums1+nums2))
    n = len(nums)
    if n % 2 == 0:
        median = (nums[n//2] + nums[n//2-1])/2
    else:
        median = nums[n//2]
    return median

if __name__=='__main__':
    nums1 = list(map(int,input("Enter nums1 items seperated by space: ").split()))
    nums2 = list(map(int,input("Enter nums2 items seperated by space: ").split()))
    Median = findMedianSortedArrays(nums1, nums2)
    print(f"The Median of given arrays is {Median}")