class Solution:
    """my bottom-up dp, 1st attempt, time n^2, space n"""
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        if not nums: return []

        nums.sort()
        dp = [1] * len(nums)
        pa = list(range(len(nums)))
        max_set = 1
        max_idx = 0

        for j in range(1, len(nums)):
            for i in range(j):
                if nums[j] % nums[i] == 0:
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        pa[j] = i
            if dp[j] > max_set:
                max_set = dp[j]
                max_idx = j

        ans = [nums[max_idx]]
        while pa[max_idx] != max_idx:
            max_idx = pa[max_idx]
            ans.append(nums[max_idx])

        return reversed(ans)

    """dp and, time n^2, space n^2"""
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        subsets = {-1: set()}

        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}

        return list(max(subsets.values(), key=len))
    