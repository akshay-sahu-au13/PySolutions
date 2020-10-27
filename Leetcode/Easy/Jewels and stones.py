## https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        count = 0
        
        
        # for i in S:
        #     for j in J:
        #         if i == j:
        #             count +=1
        # return count
        d = {}
        for i in S:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        for j in J:
            if j in d:
                count += d[j]
        
        return count 