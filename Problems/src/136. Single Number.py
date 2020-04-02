from collections import Counter
from typing import List


class Solution:
    """"""

    """time n, space n"""
    # def singleNumber(self, nums: List[int]) -> int:
    #
    #     c = Counter(nums)
    #
    #     for k, v in c.items():
    #         if v == 1:
    #             return k

    """time n, space 1"""
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for num in nums:
            ans ^= num

        return ans
