from functools import lru_cache
from typing import List


class Solution:
    """"""

    """online ans, time 2^n"""
    def lastStoneWeightII(self, stones: List[int]) -> int:
        @lru_cache(None)
        def helper(ind, curr):
            if ind == len(stones):
                return abs(curr)

            return min(helper(ind + 1, curr + stones[ind]), helper(ind + 1, curr - stones[ind]))

        return helper(0, 0)