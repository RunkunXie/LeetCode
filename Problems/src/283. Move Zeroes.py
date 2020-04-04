# %%
from typing import List


class Solution:
    """"""

    """use pop and append, time n^2"""
    # def moveZeroes(self, nums) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     count = 0
    #     n = len(nums)
    #     i = 0
    #
    #     while i < n - count:
    #
    #         if nums[i] == 0:
    #             nums.pop(i)
    #             nums.append(0)
    #             count += 1
    #         else:
    #             i += 1
    #
    #     return nums

    """use pointers, time n"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0

        while r < len(nums):

            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        return nums
