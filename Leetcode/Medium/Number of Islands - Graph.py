## https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid :
            return 
        def dfs(grid,i,j,visited):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='0':
                return
            if (i,j) in visited:
                return
            elif grid[i][j]=='1':
                visited[(i,j)]='unq'
            dfs(grid,i+1,j,visited)
            dfs(grid,i-1,j,visited)
            dfs(grid,i,j+1,visited)
            dfs(grid,i,j-1,visited)
            return




        visited={}
        island=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    if (i,j) not in visited:
                        island+=1
                        dfs(grid,i,j,visited)
        return (island)