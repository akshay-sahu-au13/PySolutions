## https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Sum = 0
        
#         for row in range(row1, row2+1):
            
#             for col in range(col1,col2+1):
                
#                 Sum += self.matrix[row][col]
                
#         return Sum

## Another approach
        
#         for row in range(row1,row2+1):
#             Sum += sum(self.mat[row][col1:col2+1])
            
#         return Sum

## Another approach

        return sum([sum(self.mat[r][col1:col2+1]) for r in range(row1, row2+1)])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)