class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        r=[0]*len(grid)
        c=[0]*len(grid[0])
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    r[i]+=1
                    c[j]+=1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    if c[j]>1 or r[i]>1:
                        ans+=1
        return ans                            

                        

        