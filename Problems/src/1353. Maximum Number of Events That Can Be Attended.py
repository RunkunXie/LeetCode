import heapq
from typing import List


class Solution:
    """"""

    """online heap greedy sol"""
    def maxEvents(self, events: List[List[int]]) -> int:
        heapq.heapify(events)
        n = day = 0
        while events:  # make sure taking the upcoming, shorestest-lasting event available from 'day'
            [s, t] = heapq.heappop(events)
            # attend this event on the s-th day
            day = s + 1  # need to increment 'day'
            n += 1  # event attended + 1
            while events and events[0][0] < day:  # update other events' available times, to start no earlier than 'day'
                [c, d] = heapq.heappop(events)
                if day <= d:
                    heapq.heappush(events, [day, d])
        return n
