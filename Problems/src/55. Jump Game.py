from typing import List


class Solution:
    """backward greedy"""
    #     def canJump(self, nums: List[int]) -> bool:

    #         n = len(nums)
    #         last_good = n - 1
    #         for i in range(n-2, -1, -1):
    #             if nums[i] >= last_good - i:
    #                 last_good = i

    #         return last_good == 0

    """forward greedy"""
    def canJump(self, nums: List[int]) -> bool:

        max_reach = nums[0]
        for i, num in enumerate(nums):
            if max_reach < i:
                return False
            max_reach = max(max_reach, i + num)

        return True


print(Solution().canJump([2, 3, 1, 1, 4]), True)
print(Solution().canJump([3, 2, 1, 0, 4]), False)
print(Solution().canJump([2, 0, 0]), True)
