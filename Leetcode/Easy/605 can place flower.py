## https://leetcode.com/problems/can-place-flowers/

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            left = (i == 0 or flowerbed[i - 1] == 0) 
            right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
            # If we're clear from the left and right and current value is 0, we can plant a flower 
            if left and right and flowerbed[i] == 0:
                n -= 1
                flowerbed[i] = 1
                # We can skip the next element since it would be invalid
                i += 1
                if n == 0:
                    return True
        return False

            