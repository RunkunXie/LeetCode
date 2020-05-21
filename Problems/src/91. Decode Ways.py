class Solution:
    """my sol under hint, time n"""
    def numDecodings(self, s: str) -> int:

        if not s:
            return 0

        dp = [0] * len(s)
        dp[0] = 1 if s[0] != '0' else 0

        for i, char in enumerate(s[1:], 1):

            if 0 < int(s[i:i + 1]) <= 9:
                dp[i] = dp[i - 1]

            if 10 <= int(s[i - 1:i + 1]) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1

        return dp[-1]
