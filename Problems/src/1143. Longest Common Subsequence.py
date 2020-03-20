class Solution:
    """DP"""

    """top-down"""
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     memo = {}
    #     m, n = len(text1), len(text2)
    #
    #     def dp(i, j):
    #         if (i, j) in memo:
    #             return memo[i, j]
    #
    #         if i == 0 or j == 0:
    #             memo[i, j] = 0
    #             return memo[i, j]
    #
    #         if text1[i-1] == text2[j-1]:
    #             ans = dp(i-1, j-1) + 1
    #         else:
    #             ans = max(dp(i, j-1), dp(i-1, j))
    #
    #         memo[i, j] = ans
    #
    #         return memo[i, j]
    #
    #     return dp(m, n)

    """top-down, use list for better performance"""
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     m, n = len(text1), len(text2)
    #     memo = [[-1] * (n + 1) for _ in range(m + 1)]
    #
    #     def dp(i, j):
    #         if memo[i][j] != -1:
    #             return memo[i][j]
    #
    #         if i == 0 or j == 0:
    #             memo[i][j] = 0
    #             return memo[i][j]
    #
    #         if text1[i-1] == text2[j-1]:
    #             ans = dp(i-1, j-1) + 1
    #         else:
    #             ans = max(dp(i, j-1), dp(i-1, j))
    #
    #         memo[i][j] = ans
    #
    #         return memo[i][j]
    #
    #     return dp(m, n)

    """bottom-up"""
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if text1[i-1] == text2[j-1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        return memo[m][n]

text1 = "abcde"
text2 = "ace"
print(Solution().longestCommonSubsequence(text1, text2), 3)
