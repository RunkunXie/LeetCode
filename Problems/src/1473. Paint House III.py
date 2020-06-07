class Solution:
    """my top-down dp sol under online hint, 1st attempt, time mnnk"""
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, j, target):

            if target == 0:
                return 0 if i == 0 else float("inf")

            elif i < target:
                return float("inf")

            elif houses[i - 1] == 0:

                # continue paint by color j
                cur_cost = cost[i - 1][j - 1] + dp(i - 1, j, target)

                # change color
                for color in range(1, n + 1):
                    if color != j:
                        cur_cost = min(cur_cost, cost[i - 1][j - 1] + dp(i - 1, color, target - 1))

                return cur_cost

            else:

                # can only paint color j, so if not j, not possible
                if j != houses[i - 1]:
                    return float("inf")

                # continue paint by color j
                cur_cost = dp(i - 1, j, target)

                # change color
                for color in range(1, n + 1):
                    if color != j:
                        cur_cost = min(cur_cost, dp(i - 1, color, target - 1))

                return cur_cost

        ans = min(dp(m, j, target) for j in range(1, n + 1))
        return ans if ans != float("inf") else -1

    """my modified top-down dp sol"""
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:

        @lru_cache(None)
        def dp(i, j, target):

            if target == 0:
                return 0 if i == 0 else float("inf")

            elif i < target:
                return float("inf")

            elif houses[i - 1] == 0:
                return min(cost[i - 1][j - 1] + dp(i - 1, color, target - (color != j))
                           for color in range(1, n + 1))

            else:

                # can only paint color j, so if not j, not possible
                if j != houses[i - 1]:
                    return float("inf")

                return min(dp(i - 1, color, target - (color != j))
                           for color in range(1, n + 1))

        ans = min(dp(m, j, target) for j in range(1, n + 1))
        return ans if ans != float("inf") else -1




