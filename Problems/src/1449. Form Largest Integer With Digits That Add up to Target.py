"""Biweekly Contest 26 - Q4"""


class Solution:
    """my sol - 1 attempt, time 9*len(target)"""
    def largestNumber(self, cost: List[int], target: int) -> str:

        item = list(range(9, 0, -1))
        weight = [cost[item[i] - 1] for i in range(9)]

        dp = [[0] * (target + 1) for _ in range(10)]
        for i in range(1, 10):
            for w in range(1, target + 1):
                if weight[i - 1] <= w and (weight[i - 1] == w or dp[i][w - weight[i - 1]] > 0):
                    dp[i][w] = max(dp[i - 1][w], dp[i][w - weight[i - 1]] * 10 + item[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]

        return str(dp[-1][-1])

    """online sol, time 9*len(target)"""
    def largestNumber(self, cost: List[int], target: int) -> str:

        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))

