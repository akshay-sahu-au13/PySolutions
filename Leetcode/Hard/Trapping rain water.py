### https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height):
        
        water = 0

        for i in range(1,len(height)-1):
            l = max(height[:i])
            r = max(height[i+1:])
            if l >0 and r>0:
                w = min(l,r) - height[i]
                if w > 0:
                    water += w        
        return water