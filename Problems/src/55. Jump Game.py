from typing import List


class Solution:
    """"""

    """my solution, time n, space 1"""
    # def canJump(self, nums: List[int]) -> bool:
    #     ans = True
    #     for num in reversed(nums[:-1]):
    #         if num == 0 and ans:
    #             ans = False
    #             count = 1
    #
    #         elif nums == 0 and not ans:
    #             count += 1
    #
    #         elif not ans:
    #             if num > count:
    #                 ans = True
    #             else:
    #                 count += 1
    #
    #     return ans

    """answer, similar to my solution"""
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        last_good = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] >= last_good - i:
                last_good = i

        return last_good == 0


print(Solution().canJump([2, 3, 1, 1, 4]), True)
print(Solution().canJump([3, 2, 1, 0, 4]), False)
print(Solution().canJump([2, 0, 0]), True)
