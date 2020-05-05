from functools import lru_cache


class Solution:
    """my dp top-down sol, time n*sqrt(n)"""
    def numSquares(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            max_num = n ** 0.5

            if int(max_num) == max_num:
                return 1

            max_num = int(max_num)

            return min([dp(n - num ** 2) + 1 for num in range(1, max_num + 1)])

        return dp(n)

    """my bottom-up dp, time n*sqrt(n)"""
    def numSquares(self, n: int) -> int:

        dp = [float("inf")] * n

        for i in range(n):

            # get current number: x, and its root
            x = i + 1
            root = int(x ** 0.5)

            # base case
            if x == root ** 2:
                dp[i] = 1
                continue

            # dp
            for r in range(1, root + 1):
                dp[i] = min(dp[i], dp[i - r ** 2] + 1)

        return dp[-1]