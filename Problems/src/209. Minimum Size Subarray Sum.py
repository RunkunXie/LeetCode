class Solution:
    """my sol, two pointers, time n"""
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:

        l, cur_sum, min_len = 0, 0, float("inf")

        for r, num in enumerate(nums):

            cur_sum += nums[r]

            while cur_sum >= s and l <= r:
                min_len = min(min_len, r - l + 1)
                cur_sum -= nums[l]
                l += 1

            if min_len == 1:
                return 1

        return min_len if min_len != float("inf") else 0
