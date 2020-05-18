class Solution:
    """TLE: my 1st sol, O(n*INT_MAX)"""
    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    #
    #     h = []
    #     int_max = 0
    #
    #     for Li, Ri, Hi in buildings:
    #
    #         while int_max <= Ri:
    #             int_max += 1
    #             h.append(0)
    #
    #         for i in range(Li, Ri + 1):
    #             h[i] = max(h[i], Hi)
    #
    #     h.append(0)
    #
    #     ans = []
    #     for i, hi in enumerate(h):
    #
    #         if hi > h[i - 1]:
    #             ans.append([i, hi])
    #         elif hi < h[i - 1]:
    #             ans.append([i - 1, hi])
    #
    #     return ans

    """online heap sol, time nlogn"""
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        sky = [[-1, 0]]
        position = set([b[0] for b in buildings] + [b[1] for b in buildings])
        live = []
        i = 0

        for t in sorted(position):

            while i < len(buildings) and buildings[i][0] <= t:
                heappush(live, (-buildings[i][2], buildings[i][1]))
                i += 1

            while live and live[0][1] <= t:
                heappop(live)

            h = -live[0][0] if live else 0
            if sky[-1][1] != h:
                sky.append([t, h])

        return sky[1:]