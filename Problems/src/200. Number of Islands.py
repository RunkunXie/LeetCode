from copy import deepcopy
from typing import List


class Solution:
    """"""

    """my previous sol"""
    # def numIslands(self, grid):
    #
    #     if not grid:
    #         return 0
    #
    #     count = 0
    #     self.m, self.n = len(grid), len(grid[0])
    #     self.grid = grid
    #     self.label = deepcopy(grid)
    #
    #     m, n = self.m, self.n
    #
    #     for i in range(m):
    #         for j in range(n):
    #             self.label[i][j] = '0'
    #
    #     for i in range(m):
    #         for j in range(n):
    #             if self.label[i][j] == '0' and self.grid[i][j] == '1':
    #                 self.dfs(i, j)
    #                 count += 1
    #
    #     return count
    #
    # def dfs(self, i, j):
    #
    #     if i < 0 or i == self.m or j < 0 or j == self.n or self.label[i][j] == '1' or self.grid[i][j] == '0':
    #         return
    #     else:
    #         self.label[i][j] = '1'
    #
    #     self.dfs(i - 1, j)
    #     self.dfs(i + 1, j)
    #     self.dfs(i, j - 1)
    #     self.dfs(i, j + 1)

    """my dfs sol, faster than 98%"""
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            grid[i][j] = '2'
            if j > 0 and grid[i][j - 1] == '1':
                dfs(i, j - 1)
            if i < m - 1 and grid[i + 1][j] == '1':
                dfs(i + 1, j)
            if j < n - 1 and grid[i][j + 1] == '1':
                dfs(i, j + 1)
            if i > 0 and grid[i - 1][j] == '1':
                dfs(i - 1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1

        return count


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "1", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "1"]]
grid = [["1", "1", "1"]]
s = Solution()
print(s.numIslands(grid))
