"""Biweekly Contest 26 - Q1"""

class Solution:
    """my sol - first attempt"""
    def maxPower(self, s: str) -> int:

        cur = 1
        power = 1

        for i in range(1, len(s)):

            if s[i] == s[i - 1]:
                cur += 1
            else:
                cur = 1

            power = max(power, cur)

        return power

    """online sol - 1 line"""
    def maxPower(self, s: str) -> int:

        return max(len(list(b)) for a, b in itertools.groupby(s))

