
### https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) ->           List[List[int]]:
        l = len(colsum)
        row1 = [0]*l
        row2 = [0]*l
        
        if sum(colsum) != upper+lower:
            return []
        
        for i in range(l):
            
            if colsum[i] == 2:
                row1[i] = 1
                row2[i] = 1
                lower -= 1
                upper -= 1
            elif colsum[i] == 1:
                if upper >= lower:
                    row1[i] = 1
                    row2[i] = 0
                    upper -= 1
            
                else:
                    row1[i] = 0
                    row2[i] = 1
                    lower -= 1
                    
            else:
                row1[i] = 0
                row2[i] = 0
            
        if upper != 0 or lower != 0:
            return []
        return [row1,row2]