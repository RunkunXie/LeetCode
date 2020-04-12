from typing import List


class Solution:
    """"""

    """ans using sort, time nlogn, space 1 or n
    
        this one is easy and intuitive to come up with
    """
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     if not nums:
    #         return 0
    #
    #     nums.sort()
    #
    #     longest_streak = 1
    #     current_streak = 1
    #
    #     for i in range(1, len(nums)):
    #         if nums[i] != nums[i-1]:
    #             if nums[i] == nums[i-1]+1:
    #                 current_streak += 1
    #             else:
    #                 longest_streak = max(longest_streak, current_streak)
    #                 current_streak = 1
    #
    #     return max(longest_streak, current_streak)

    """ans, using set, time n, space n"""
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak