from heapq import *
from typing import List


class Solution:
    """"""

    """my sol, time nlogn"""
    def lastStoneWeight(self, stones: List[int]) -> int:

        if not stones:
            return 0

        h = [-s for s in stones]
        heapify(h)

        while len(h) > 1:
            print(h)
            s1 = -heappop(h)
            s2 = -heappop(h)

            if s1 != s2:
                heappush(h, -abs(s1 - s2))

        if len(h) == 1:
            return -h[0]

        return 0