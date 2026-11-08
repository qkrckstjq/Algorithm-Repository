class Solution:
    dy = [0, 0, 1, -1]
    dx = [1, -1, 0, 0]


    def countServers(self, grid: list[list[int]]) -> int:
        visit = [[0 for _ in range(len(grid[i]))] for i in range(len(grid))]
        result = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visit[i][j] == 0 and grid[i][j] == 1:
                    t_cnt, cnt = self.dfs(i, j, grid, visit)
                    # print(visit)
                    if t_cnt > 1:
                        result += cnt

        return result

    def dfs(self, i, j, grid, visit):
        visit[i][j] = 1
        total_result = 1
        result = 1
        

        u_i = i - 1
        d_i = i + 1
        l_j = j - 1
        r_j = j + 1

        while u_i >= 0 or d_i < len(grid) or l_j >= 0 or r_j < len(grid[0]):
            if u_i >= 0:
                if grid[u_i][j] == 1:
                    total_result += 1
                    if visit[u_i][j] == 0:
                        result += 1
                        visit[u_i][j] = 1
                u_i -= 1
            
            if d_i < len(grid):
                if grid[d_i][j] == 1:
                    total_result += 1
                    if visit[d_i][j] == 0:
                        result += 1
                        visit[d_i][j] = 1
                d_i += 1

            if l_j >= 0:
                if grid[i][l_j] == 1:
                    total_result += 1
                    if visit[i][l_j] == 0:
                        result += 1
                        visit[i][l_j] = 1
                l_j -= 1

            if r_j < len(grid[0]):
                if grid[i][r_j] == 1:
                    total_result += 1
                    if visit[i][r_j] == 0:
                        result += 1
                        visit[i][r_j] = 1
                r_j += 1
                    
            # print(u_i, d_i, l_j, r_j)

        return total_result, result