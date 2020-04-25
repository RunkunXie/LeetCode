from functools import lru_cache
from typing import List

class Solution:
    """my dp sol, bottom up, time n^3"""
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for l in range(n - 1, -1, -1):
            for r in range(l, n):

                if l == r or l + 1 == r:
                    continue

                elif l + 2 == r:
                    dp[l][r] = nums[l] * nums[l + 1] * nums[r]

                else:
                    dp[l][r] = max([nums[l] * nums[i] * nums[r] + dp[l][i] + dp[i][r] for i in range(l + 1, r)])

        return dp[0][n - 1]

    """my dp sol, top-down"""
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dp(l, r):

            if l == r or l + 1 == r:
                return 0

            if l + 2 == r:
                return nums[l] * nums[l + 1] * nums[r]

            return max([nums[l] * nums[i] * nums[r] + dp(l, i) + dp(i, r)
                        for i in range(l + 1, r)])

        return dp(0, n - 1)

