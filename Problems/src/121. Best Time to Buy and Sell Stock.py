class Solution:
    """"""

    """One Pass approach, time n, space 1"""
    def maxProfit(self, prices) -> int:

        if not prices:
            return 0

        max_profit = 0
        low_p = prices[0]

        for p in prices[1:]:
            low_p = min(low_p, p)
            max_profit = max(max_profit, p - low_p)

        return max_profit