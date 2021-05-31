# Q-1 ) Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/submissions/
# (5 marks)
# Given two integer arrays nums1 and nums2, return an array of their
# intersection. Each element in the result must be unique and you may return
# the result in any order.
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]


def intersection(nums1, nums2):
    
    uniqueList = []
    nums1 = sorted(set(nums1))
    nums2 = sorted(set(nums2))
    
    i = j = 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            uniqueList.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]: 
            j += 1
        else: 
            i += 1
            
    return uniqueList


if __name__ == "__main__" :

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    ans = intersection(nums1, nums2)
    print(ans)