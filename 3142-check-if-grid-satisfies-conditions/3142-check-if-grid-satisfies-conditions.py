class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        l=len(grid[0])
        for i in range(len(grid)):
            for j in range(l):
                if i+1<len(grid):
                    if grid[i+1][j]!=grid[i][j]:
                        return False
                if j+1<l:
                    if grid[i][j+1]==grid[i][j]:
                        return False 
        return True                       



        