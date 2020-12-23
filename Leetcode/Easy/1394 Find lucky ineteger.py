## https://leetcode.com/problems/find-lucky-integer-in-an-array/

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = {}
        a = []
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        print(d)
        for x,y in d.items():
            if x == y:
                a.append(x)

        return max(a) if a else -1