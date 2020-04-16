from heapq import *


def minimumTime(ability, processes):
    # Write your code here
    h = [-a for a in ability]
    heapify(h)
    count = 0

    while processes > 0:
        tmp = heappop(h)
        processes += tmp
        heappush(h, -int(-tmp / 2))
        count += 1

    return count



