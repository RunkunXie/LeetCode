

class Solution:
    def regionsBySlashes(self, grid) -> int:

        # size of grid: (n * n), size of label: (3*n, 3*n)
        self.n = len(grid)
        self.N = self.n * 3

        # label = 0: blank space
        self.label = [[0 for i in range(self.N)] for j in
                      range(self.N)]  # can't use "self.label = [[0] * self.N] * self.N"
        self.count = 0

        # label = 1: divide line
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == '/':
                    self.label[i * 3 + 0][j * 3 + 2] = 1
                    self.label[i * 3 + 1][j * 3 + 1] = 1
                    self.label[i * 3 + 2][j * 3 + 0] = 1
                elif grid[i][j] == '\\':
                    self.label[i * 3 + 0][j * 3 + 0] = 1
                    self.label[i * 3 + 1][j * 3 + 1] = 1
                    self.label[i * 3 + 2][j * 3 + 2] = 1

        # dps on blank space, mark passed space by 2
        for i in range(self.N):
            for j in range(self.N):
                if self.label[i][j] == 0:
                    self.dfs(i, j)
                    self.count += 1

        return self.count

    def dfs(self, i, j):

        # out-of-bound, touch line, been there before - return
        if (i < 0) or (i == self.N) or (j < 0) or (j == self.N) or (
                self.label[i][j] == 1) or (self.label[i][j] == 2):
            return

        # not been there before - label the position, then continue
        self.label[i][j] = 2

        self.dfs(i + 1, j)
        self.dfs(i - 1, j)
        self.dfs(i, j + 1)
        self.dfs(i, j - 1)


grid = [" /","/ "]
print(Solution().regionsBySlashes(grid))



