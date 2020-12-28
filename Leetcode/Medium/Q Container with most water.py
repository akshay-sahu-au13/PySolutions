## https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:

        p1,p2 = 0,len(height) - 1

        max1 = 0
        
        while p1 < p2:
            area  = min(height[p1],height[p2]) * (p2-p1)
            max1 = area if area > max1 else max1
            if (height[p1] < height[p2]):
                p1 +=1;
            else:
                p2 -=1;
            
        return max1