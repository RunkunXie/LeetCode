class Solution:
    """"""

    """n time, 1 space"""
    def maxSubArray(self, nums) -> int:
        crt_sum = max_sum = nums[0]

        for num in nums[1:]:
            crt_sum = max(num, num + crt_sum)
            max_sum = max(max_sum, crt_sum)

        return max_sum