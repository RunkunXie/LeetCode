from collections import Counter
from typing import List
import heapq


class Solution:
    """"""

    """my sol, nlogn"""
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     c = list(Counter(nums).items())
    #     sort_c = sorted(c, key=lambda x: x[1], reverse=True)
    #
    #     return [sort_c[i][0] for i in range(k)]

    """online sol, nlogn"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]

    """ans, nlogk"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
