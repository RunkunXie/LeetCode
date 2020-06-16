# %%
from typing import List


class Solution:
    """my sol under hint, time n space 1"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = -1
        for right in range(len(nums)):
            if nums[right] != 0:
                left += 1
                nums[left], nums[right] = nums[right], nums[left]

    """my sol, 2nd attempt, time n^2, space n"""
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        start, end = 0, len(nums)
        while start < end:
            if nums[start] == 0:
                nums[start:end - 1] = nums[start + 1:end]
                end -= 1
                nums[end] = 0
            else:
                start += 1

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
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     l = r = 0
    #
    #     while r < len(nums):
    #
    #         if nums[r] != 0:
    #             nums[l], nums[r] = nums[r], nums[l]
    #             l += 1
    #         r += 1
    #
    #     return nums
