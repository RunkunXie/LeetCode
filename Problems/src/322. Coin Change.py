from typing import List


class Solution:
    """"""

    """my dp bottom up sol, time amount * len(coins)"""
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #
    #     # corner case 1
    #     if not coins:
    #         return -1
    #
    #     # corner case 2
    #     if len(coins) is 1:
    #         return -1 if amount % coins[0] else int(amount / coins[0])
    #
    #     # corner case 3:
    #     if amount == 0:
    #         return 0
    #
    #     # dp solution
    #     memo = [-1] * (amount + 1)
    #     coin_set = set(coins)
    #
    #     for x in range(1, len(memo)):
    #         if x in coin_set:
    #             memo[x] = 1
    #         else:
    #             min_num = None
    #             for c in coin_set:
    #                 if x - c > 0 and memo[x - c] > 0:
    #                     cur_num = memo[x - c] + 1
    #                     if min_num is None:
    #                         min_num = cur_num
    #                     else:
    #                         min_num = min(cur_num, min_num)
    #
    #             if min_num is not None:
    #                 memo[x] = min_num
    #
    #     return memo[amount]

    """dp bottom-up ans, time amount * len(coins), MUCH simpler, not intuitive"""
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
