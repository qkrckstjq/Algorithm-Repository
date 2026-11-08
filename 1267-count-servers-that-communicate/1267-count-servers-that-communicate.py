class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        c=0
        for i in grid:
            sm=sum(i)
            if sm==1:
                t=0
                for idx, n in enumerate(i):
                    if n == 1:
                        t = idx
                        break
                cc=0
                for j in range(len(grid)):
                    if grid[j][t]==1:
                        cc+=1
                if cc<2:
                    c-=1
            c+=sm
        return c