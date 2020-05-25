class Solution:
    """my sol, 1 attempt, time n^2, space n^2"""
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        n, m = len(A), len(B)

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if dp[i - 1][j] == dp[i][j - 1] == dp[i - 1][j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

        return dp[-1][-1]

    """my modified sol - based on online sol, time n^2, space n"""
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        n, m = len(A), len(B)
        dp = defaultdict(int)

        for i in range(n):
            for j in range(m)[::-1]:
                if A[i] == B[j]: dp[j] = dp[j - 1] + 1
            for j in range(m):
                dp[j] = max(dp[j], dp[j - 1])

        return dp[m - 1]
