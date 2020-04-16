from typing import List
from collections import Counter


class Solution:
    """"""

    """online sol from c++"""
    # def subsetA(self, arr):
    #     x = sorted(arr)
    #
    #     # initialize
    #     last = 0
    #     max_weight = 0
    #     value = []
    #     weight = []
    #     actual = []
    #
    #     # build lists
    #     for i in x:
    #         max_weight += i
    #         if len(value) == 0 or i != last:
    #             value.append(1)
    #             weight.append(i)
    #             actual.append(i)
    #         else:
    #             value[-1] += 1
    #             weight[-1] += i
    #         last = i
    #     max_weight = int((max_weight - 1) / 2)
    #
    #     # dp to find set B
    #     dp = [[0 for i in range(max_weight + 1)] for j in range(len(value))]
    #     for i in range(len(value)):
    #         for w in range(max_weight + 1):
    #             if i == 0:
    #                 skip = 0
    #             else:
    #                 skip = dp[i - 1][w]
    #             include = 0
    #             if weight[i] <= w:
    #                 include = value[i]
    #                 if i > 0:
    #                     include += dp[i - 1][w - weight[i]]
    #             dp[i][w] = max(include, skip)
    #
    #     # results of set B
    #     w = max_weight
    #     result = []
    #     for i in range(len(value) - 1, 0, -1):
    #         if dp[i - 1][w] != dp[i][w]:
    #             result.append(actual[i])
    #             w -= weight[i]
    #     if w > 0:
    #         result.append(actual[0])
    #
    #     # get set A
    #     A = []
    #     for i in x:
    #         if i not in result:
    #             A.append(i)
    #     return A

    """my sol"""
    def subsetA(self, arr: List[int]) -> List:
        arr = sorted(arr)
        c = Counter(arr)

        # knapsack
        actual = list(c.keys())
        values = list(c.values())
        weight = [actual[i] * values[i] for i in range(len(c))]

        # dp for set B
        max_weight = int((sum(weight) - 1) / 2)
        dp = [[0] * (max_weight + 1) for _ in range(len(c) + 1)]
        for i in range(1, len(c) + 1):
            for w in range(1, max_weight + 1):
                if weight[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + values[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]

        # get set B
        set_B = set()
        w = max_weight
        for i in range(len(c), 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                set_B.add(actual[i - 1])
                w -= weight[i - 1]

        # get set A
        A = []
        for i in arr:
            if i not in set_B:
                A.append(i)
        return A


print(Solution().subsetA([3, 7, 5, 6, 2]), [6, 7])
print(Solution().subsetA([2, 3, 4, 4, 5, 9, 7, 8, 6, 10, 4, 5, 10, 10, 8, 4, 6, 4, 10, 1]), [8, 8, 9, 10, 10, 10, 10])

print(Solution().subsetA([2, 5, 5, 9]), [2, 9])
print(Solution().subsetA([2, 2, 4, 5, 5, 11]), [4, 11])
print(Solution().subsetA([5, 5, 5, 10, 10, 10, 11]), [10, 10, 10])
