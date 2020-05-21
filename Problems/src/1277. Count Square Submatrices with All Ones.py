class Solution:
    """my top-down dp, time n^2"""
    def countSquares(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dp(i, j):

            # base case, 0
            if matrix[i][j] == 0:
                return 0

            # base case, corner and side
            if i == 0 or j == 0:
                return 1

            # transition function
            return 1 + min(dp(i - 1, j),
                           dp(i, j - 1),
                           dp(i - 1, j - 1))

        return sum(dp(i, j) for i in range(m) for j in range(n)) if matrix and matrix[0] else 0


class Solution:
    """my bottom-up dp, time n^2"""
    def countSquares(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        dp = [[0] * n for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):

                # base case, 1
                if matrix[i][j] == 1:
                    dp[i][j] = 1

                    # if not at corner or side
                    if i > 0 and j > 0:
                        dp[i][j] += min(dp[i - 1][j],
                                        dp[i][j - 1],
                                        dp[i - 1][j - 1])

                # sum up
                ans += dp[i][j]

        return ans





