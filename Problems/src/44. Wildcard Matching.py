class Solution:
    """my dp sol, 1st attempt, time s*p"""
    def isMatch(self, s: str, p: str) -> bool:

        ns, np = len(s), len(p)
        dp = [[False] * (ns + 1) for _ in range(np + 1)]
        dp[0][0] = True

        for i in range(1, np + 1):
            for j in range(ns + 1):

                if j == 0:
                    dp[i][j] = p[i - 1] == '*' and dp[i - 1][j]

                elif p[i - 1] == '*' and (dp[i - 1][j] or dp[i][j - 1]):
                    dp[i][j] = True

                elif match := p[i - 1] == '?' or p[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]

    """online sol, similar to answer, 
    best time min(S,P), average slogp, see paper: https://arxiv.org/pdf/1407.0950.pdf
    """
    def isMatch(self, s: str, p: str) -> bool:

        sn, pn = len(s), len(p)
        si = pi = 0
        save_si, save_pi = None, None
        while si < sn:
            if pi < pn and (p[pi] == '?' or p[pi] == s[si]):
                si += 1
                pi += 1
            elif pi < pn and p[pi] == '*':
                # Meet "*", save si and pi, searching for next character
                save_si, save_pi = si + 1, pi
                pi += 1
            elif save_pi is not None:
                # Dead end, restore si and pi, carry on.
                si, pi = save_si, save_pi
            else:
                return False

        # The remaining characters in the pattern should all be '*' characters
        return all(x == '*' for x in p[pi:])
