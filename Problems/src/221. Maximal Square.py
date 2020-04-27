from typing import List
from collections import deque


class Solution:
    """my sol using Q84 modified, time n^2"""
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            ans = max(ans, self.maxSquareinHeights(heights))
        return ans

    @staticmethod
    def maxSquareinHeights(heights):

        dq = deque([-1])
        ans = 0

        for i, h in enumerate(heights):
            while dq and heights[dq[-1]] > h:
                cur_area = min(heights[dq.pop()], i - dq[-1] - 1) ** 2
                ans = max(ans, cur_area)
            dq.append(i)

        return ans

    """my sol after hint, using bottom-up dp, time n^2"""
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):

                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])

                elif matrix[i][j] == '1':
                    dp[i][j] = min(dp[i - 1][j],
                                   dp[i - 1][j - 1],
                                   dp[i][j - 1]) + 1

                ans = max(ans, dp[i][j] ** 2)

        return ans

