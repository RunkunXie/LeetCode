class Solution:

    """my top-down dp, 2nd attempt"""
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        @lru_cache(None)
        def dp(i, target):
            if i == -1:
                return target == 0

            return dp(i - 1, target + nums[i]) + dp(i - 1, target - nums[i])

        return dp(len(nums) - 1, S)

    """my sol, bottom up dp"""
    #     def findTargetSumWays(self, nums: List[int], S: int) -> int:

    #         if abs(S) > 1000:
    #             return 0

    #         n = len(nums)

    #         dp = [[0] * (n + 1) for _ in range(2001)]
    #         dp[1000][0] = 1

    #         for j in range(1, n + 1):
    #             for i in range(2001):
    #                 if i-nums[j-1] >= 0 and dp[i-nums[j-1]][j-1] > 0:
    #                     dp[i][j] += dp[i-nums[j-1]][j-1]
    #                 if i+nums[j-1] <= 2000 and dp[i+nums[j-1]][j-1] > 0:
    #                     dp[i][j] += dp[i+nums[j-1]][j-1]

    #         return dp[1000+S][n]

    """my sol, top-down dp"""
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        # corner case
        if abs(S) > 1000:
            return 0

        n = len(nums)
        memo = {(1000, 0): 1}

        # top-down dp
        def dp(i, j):

            # memorized case
            if (i, j) in memo:
                return memo[i, j]

            # corner case
            if i < 0 or i > 2000:
                return 0

            # base case
            if j == 0:
                ans = 0
                if i == 1000:
                    ans = 1

            # dp case
            elif j > 0:
                ans = dp(i - nums[j - 1], j - 1) + dp(i + nums[j - 1], j - 1)

            memo[i, j] = ans
            return ans

        return dp(1000 + S, n)