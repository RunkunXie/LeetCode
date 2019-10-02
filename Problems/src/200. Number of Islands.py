from copy import deepcopy

class Solution:
    def numIslands(self, grid):

        if not grid:
            return 0

        count = 0
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.label = deepcopy(grid)

        m, n = self.m, self.n

        for i in range(m):
            for j in range(n):
                self.label[i][j] = '0'

        for i in range(m):
            for j in range(n):
                if self.label[i][j] == '0' and self.grid[i][j] == '1':
                    self.dfs(i, j)
                    count += 1

        return count

    def dfs(self, i, j):

        if i < 0 or i == self.m or j < 0 or j == self.n or self.label[i][j] == '1' or self.grid[i][j] == '0':
            return
        else:
            self.label[i][j] = '1'

        self.dfs(i - 1, j)
        self.dfs(i + 1, j)
        self.dfs(i, j - 1)
        self.dfs(i, j + 1)


grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "1", "0"], ["0", "0", "0", "0", "0"], ["0", "0", "0", "0", "1"]]
grid = [["1", "1", "1"]]
s = Solution()
print(s.numIslands(grid))