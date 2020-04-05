from typing import List


class Solution:
    """"""

    """one pass, time n, space 1"""
    # def maxProfit(self, prices: List[int]) -> int:
    #
    #     if not prices:
    #         return 0
    #
    #     total_profit = 0
    #     cur_max_profit = 0
    #     low_p = prices[0]
    #
    #     for i in range(1, len(prices)):
    #
    #         if prices[i] < prices[i - 1]:
    #             low_p = prices[i]
    #             total_profit += cur_max_profit
    #             cur_max_profit = 0
    #
    #         else:
    #             cur_max_profit = prices[i] - low_p
    #
    #     total_profit += cur_max_profit
    #
    #     return total_profit

    """answer: one pass, time n, space 1"""
    def maxProfit(self, prices: List[int]) -> int:

        if not prices:
            return 0

        total_profit = 0
        for i in range(1, len(prices)):
            total_profit += max(prices[i] - prices[i-1], 0)

        return total_profit
