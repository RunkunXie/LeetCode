class Solution:

    """my top-down dp sol, 2nd attempt, solved!"""
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def dp(i, j):

            if j == -1:
                return i + 1

            if i == -1:
                return j + 1

            return min(dp(i - 1, j - 1) + (word1[i] != word2[j]),
                       dp(i - 1, j) + 1,
                       dp(i, j - 1) + 1)

        return dp(len(word1) - 1, len(word2) - 1)

    """my bottom up dp sol, 2nd attempt"""
    def minDistance(self, word1: str, word2: str) -> int:

        n, m = len(word1), len(word2)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(m + 1):

                if i == 0:
                    dp[i][j] = j

                elif j == 0:
                    dp[i][j] = i

                else:
                    dp[i][j] = min(dp[i - 1][j] + 1,
                                   dp[i][j - 1] + 1,
                                   dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))

        return dp[n][m]

    """my sol, bottom up dp"""
    # def minDistance(self, word1: str, word2: str) -> int:
    #
    #     n, m = len(word1), len(word2)
    #
    #     dp = [[0] * (m + 1) for _ in range(n + 1)]
    #
    #     for i in range(n + 1):
    #         for j in range(m + 1):
    #
    #             if i == 0 and j == 0:
    #                 continue
    #
    #             elif i == 0 or j == 0:
    #                 dp[i][j] = max(i, j)
    #
    #             else:
    #
    #                 if word1[i - 1] == word2[j - 1]:
    #                     dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
    #                 else:
    #                     dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    #
    #     return dp[n][m]

    """
    dp, top-down
    For this question, we need iter all cases, so top-down is slower than bottom-up

    :param word1:
    :param word2:
    :return:
    """
    # def minDistance(self, word1: str, word2: str) -> int:
    #     m, n = len(word1), len(word2)
    #
    #     memo = {}
    #
    #     def dp(i, j):
    #
    #         if (i, j) in memo:
    #             return memo[i, j]
    #
    #         # boundary
    #         if i == 0 or j == 0:
    #             memo[i, j] = max(i, j)
    #             return memo[i, j]
    #
    #         # when last char is the same
    #         if word1[i - 1] == word2[j - 1]:
    #             ans = min(dp(i - 1, j - 1), dp(i - 1, j) + 1, dp(i, j - 1) + 1)
    #         else:
    #             ans = min(dp(i - 1, j - 1) + 1, dp(i - 1, j) + 1, dp(i, j - 1) + 1)
    #
    #         memo[i, j] = ans
    #
    #         return ans
    #
    #     return dp(m, n)


print(Solution().minDistance("abc","bdef"), 4)
print(Solution().minDistance("abcde","adcbef"), 3)
print(Solution().minDistance("prosperity", "properties"), 4)
