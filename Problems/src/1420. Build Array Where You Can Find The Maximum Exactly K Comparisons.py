from functools import lru_cache
import itertools


class Solution:
    """online sol, dp top-down, time n * m * k * m"""
    # def numOfArrays(self, n: int, m: int, k: int) -> int:
    #     @lru_cache(None)
    #     def dp(arr_len, max_num, cost):
    #         if arr_len == 1:
    #             return 1 if cost == 1 else 0
    #
    #         ans = dp(arr_len - 1, max_num, cost) * max_num
    #
    #         ans += sum([dp(arr_len - 1, num, cost - 1) for num in range(1, max_num)])
    #
    #         return ans % 1000000007
    #
    #     return sum([dp(n, i, k) for i in range(1, m + 1)]) % 1000000007

    """online sol, dp bottom-up"""
    def numOfArrays(self, N: int, M: int, K: int) -> int:

        dp = [[[0 for _ in range(M + 1)] for _ in range(K + 1)] for _ in range(N + 1)]

        # the array has length of 1, and 1 jump, only 1 way to do that, for any k
        for k in range(1, M + 1):
            dp[1][1][k] = 1

        for i, j, k in itertools.product(range(1, N + 1), range(1, K + 1), range(M + 1)):
            dp[i][j][k] += dp[i - 1][j][k] * k
            dp[i][j][k] += sum(dp[i - 1][j - 1][1:k])

        return sum(dp[N][K][1:]) % (10 ** 9 + 7)
