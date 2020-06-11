from functools import lru_cache


class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """

    """my top-down dp, 3rd attempt after look at 1st attempt: LC Q44"""
    def isMatch(self, s, p):
        # write your code here

        @lru_cache(None)
        def dp(i, j):

            if j == -1:
                return i == -1

            elif i == -1 and j >= 0:
                return dp(i, j - 1) if p[j] == "*" else False

            elif p[j] != "*":
                return p[j] in ('?', s[i]) and dp(i - 1, j - 1)

            else:
                return dp(i - 1, j) or dp(i, j - 1)

        return dp(len(s) - 1, len(p) - 1)

    """my top-down dp, 2nd attempt, very slow"""
    def isMatch(self, s, p):
        # write your code here

        @lru_cache(None)
        def dp(i, j):

            if j == -1:
                return i == -1

            elif i == -1 and j >= 0:
                return dp(i, j - 1) if p[j] == "*" else False

            elif p[j] != "*":
                return p[j] in ('?', s[i]) and dp(i - 1, j - 1)

            else:
                return any(dp(_, j - 1) for _ in range(-1, i + 1))

        return dp(len(s) - 1, len(p) - 1)
