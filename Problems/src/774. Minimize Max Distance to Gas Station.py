class Solution:
    """
        n < 2000
        k < 100000
    """

    """my heap sol, 1st attempt, time klogn, TLE"""
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        gap = [[stations[i] - stations[i + 1], 1] for i in range(len(stations) - 1)]
        heapify(gap)

        for i in range(K):
            max_gap, num = heappop(gap)
            heappush(gap, [max_gap * num / (num + 1), num + 1])

        return -gap[0][0]

    """my bisearch sol under hint, time nlogw, w=station[-1]"""
    def minmaxGasDist(self, stations: List[int], K: int) -> float:

        start = 0
        end = stations[-1]

        while end - start > 1e-6:
            mid = start + (end - start) / 2

            add_station = 0
            for i in range(len(stations) - 1):
                if stations[i + 1] - stations[i] > mid:
                    add_station += (stations[i + 1] - stations[i]) // mid

                if add_station > K:
                    start = mid
                    break
            else:
                end = mid

        return end

    """my bisearch sol2 under hint, time nlogw, w=station[-1]"""
    def minmaxGasDist(self, stations: List[int], K: int) -> float:

        start = 0
        end = stations[-1]

        while end - start > 1e-6:
            mid = start + (end - start) / 2

            # replace for loop by comprehension
            add_station = sum((stations[i + 1] - stations[i]) // mid
                              for i in range(len(stations) - 1))

            if add_station > K:
                start = mid
            else:
                end = mid

        return end