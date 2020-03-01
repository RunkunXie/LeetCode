class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     """
    #     dp, bottom-up
    #     :param word1:
    #     :param word2:
    #     :return:
    #     """
    #
    #     m, n = len(word1), len(word2)
    #
    #     dp = [[0] * (n + 1) for _ in range(m + 1)]
    #
    #     # boundary
    #     for i in range(m + 1):
    #         dp[i][0] = i
    #     for j in range(n + 1):
    #         dp[0][j] = j
    #
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #
    #             # when last char is the same
    #             if word1[i - 1] == word2[j - 1]:
    #                 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    #             else:
    #                 dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    #
    #     return dp[m][n]

    def minDistance(self, word1: str, word2: str) -> int:
        """
        dp, top-down
        For this question, we need iter all cases, so top-down is slower than bottom-up

        :param word1:
        :param word2:
        :return:
        """

        m, n = len(word1), len(word2)

        memo = {}

        def dp(i, j):

            if (i, j) in memo:
                return memo[i, j]

            # boundary
            if i == 0 or j == 0:
                memo[i, j] = max(i, j)
                return memo[i, j]

            # when last char is the same
            if word1[i - 1] == word2[j - 1]:
                ans = min(dp(i - 1, j - 1), dp(i - 1, j) + 1, dp(i, j - 1) + 1)
            else:
                ans = min(dp(i - 1, j - 1) + 1, dp(i - 1, j) + 1, dp(i, j - 1) + 1)

            memo[i, j] = ans

            return ans

        return dp(m, n)


print(Solution().minDistance("abc","bdef"), 4)
print(Solution().minDistance("abcde","adcbef"), 3)
print(Solution().minDistance("prosperity", "properties"), 4)
