class Solution:

    """my bisect sol modified from online sol, 2nd attempt, time nlogn"""
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = []
        for x in nums:
            i = bisect_left(tails, x)
            if i == len(tails): tails.append(x)
            else: tails[i] = x

        return len(tails)

    """my bottom-up dp, 2nd attempt"""
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for j in range(1, len(nums)):
            dp[j] = max(dp[i] + 1 if nums[i] < nums[j] else 1 for i in range(j))

        return max(dp) if dp else 0

    """my top-down dp, 2nd attempt"""
    def lengthOfLIS(self, nums: List[int]) -> int:

        @lru_cache(None)
        def dp(j):

            ans = 1
            if j == 0:
                return ans

            for i in range(j):
                if nums[i] < nums[j]:
                    ans = max(ans, dp(i) + 1)

            return ans

        return max(dp(j) for j in range(len(nums))) if nums else 0

    """TODO: online bi select sol, time nlogn"""
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        import collections
        tail_dp = []  # stores the smallest tail of element with LIS with length i
        history = collections.defaultdict(list)
        for x in nums:
            idx = bisect.bisect_left(tail_dp, x)
            if idx == len(tail_dp):
                tail_dp.append(x)
            else:
                tail_dp[idx] = x
            # Every iteration reconstruct from smaller increasing subsequence
            history[idx + 1] = history[idx] + [x]

            print(tail_dp)
            print(history)

        LIS = history[len(tail_dp)]  # This is a valid LIS.

        return len(tail_dp)