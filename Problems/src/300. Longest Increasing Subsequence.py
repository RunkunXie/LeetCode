class Solution:
    """online dp sol, time n^2"""
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0

        # dp[i]: Longest Increasing Subsequence of nums[0] ~ nums[i],
        # which containing nums[i]
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

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