from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if i == 0:
                    if j == 0:
                        continue
                    grid[i][j] += grid[i][j - 1]

                else:
                    if j == 0:
                        grid[i][j] += grid[i - 1][j]
                    else:
                        grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]