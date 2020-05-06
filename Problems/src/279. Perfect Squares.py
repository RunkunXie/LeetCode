from functools import lru_cache


class Solution:
    """my dp top-down sol, time n*sqrt(n), time 6000ms"""
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


class Solution:
    """answer, better time 64ms"""
    def numSquares(self, n):

        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count

        """ans, dp, time 4000ms"""
        def numSquares(self, n):
            """
            :type n: int
            :rtype: int
            """
            square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]

            dp = [float('inf')] * (n + 1)
            # bottom case
            dp[0] = 0

            for i in range(1, n + 1):
                for square in square_nums:
                    if i < square:
                        break
                    dp[i] = min(dp[i], dp[i - square] + 1)

            return dp[-1]