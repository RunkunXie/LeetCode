class Solution:
    """my dp sol under hint, time n, space n"""
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[:2])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

