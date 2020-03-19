# %%
class Solution:
    """"""

    """use pop and append"""
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

    """use pointers"""
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        l = r = 0

        while r < n:

            if nums[r] != 0:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp
                l += 1
            r += 1

        return nums
