## https://leetcode.com/problems/container-with-most-water/submissions/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        ## This approach works but giving TLE for very large inputs
        # area = []
        # count = 1
        # last = height[-1]
        # L = len(height)
        # for i in range(L):
        #     for j in range(i+1,L):
        #         ar = min(height[i],height[j])*(j-i)
        #         area.append(ar)
        #     # print(area)
        # return max(area)
        
    #### two pointer approach uisng hints
        
        p1 = 0
        p2 = len(height) - 1
        max1 = 0
        
        while p1 < p2:
            area  = min(height[p1],height[p2]) * (p2-p1)
            max1 = max(max1,area)
            if (height[p1] < height[p2]):
                p1 +=1;
            else:
                p2 -=1;
            
        return max1