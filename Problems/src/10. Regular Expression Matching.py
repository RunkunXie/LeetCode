class Solution:

    """my top-down dp sol, 4th attempt"""
    def isMatch(self, text, pattern):
        s, p = text, pattern

        @lru_cache(None)
        def dp(i, j):

            if j == -1:
                return i == -1

            elif i == -1:
                return dp(i, j - 2) if j > 0 and p[j] == '*' else False

            else:
                if p[j] != '*':
                    return dp(i - 1, j - 1) if p[j] in (s[i], '.') else False
                else:
                    if j == 0:
                        return False
                    elif p[j - 1] not in (s[i], '.'):
                        return dp(i, j - 2)
                    else:
                        return dp(i, j - 2) or dp(i - 1, j)

        return dp(len(s) - 1, len(p) - 1)

    """my sol, bottom-up dp, forward, 2/3 attempt"""
    def isMatch(self, text, pattern):

        s, p = text, pattern
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(1, n + 1):

                if i == 0:
                    if p[j - 1] != "*":
                        ans = False
                    else:
                        ans = j >= 2 and dp[i][j - 2]

                else:
                    if p[j - 1] != "*":
                        ans = p[j - 1] in [s[i - 1], '.'] and dp[i - 1][j - 1]
                    else:
                        if j == 1:
                            ans = 0
                        elif p[j - 2] in [s[i - 1], '.']:
                            ans = dp[i][j - 2] or dp[i - 1][j]
                        else:
                            ans = dp[i][j - 2]

                dp[i][j] = ans

        return dp[m][n]

    """Top-down dp backward solution."""
    # def isMatch(self, s: str, p: str) -> bool:
    #
    #     memo = {}
    #     m, n = len(s), len(p)
    #
    #     def dp(i, j):
    #
    #         # Top-down, save ans in memo
    #         if (i, j) not in memo:
    #
    #             # solution
    #             if j == n:
    #                 ans = i == m
    #
    #             else:
    #                 first_match = i < m and p[j] in [s[i], '.']
    #
    #                 if j + 1 < n and p[j + 1] == '*':
    #                     ans = (dp(i, j + 2) or
    #                            first_match and dp(i + 1, j))
    #                 else:
    #                     ans = first_match and dp(i + 1, j + 1)
    #
    #             memo[i, j] = ans
    #
    #         return memo[i, j]
    #
    #     return dp(0, 0)

    """Bottom-up DP backward solution."""
    # def isMatch(self, s: str, p: str) -> bool:
    #
    #     m, n = len(s), len(p)
    #     dp = [[False] * (n+1) for i in range(m+1)]
    #     dp[m][n] = True
    #
    #     for i in range(m, -1, -1):
    #         for j in range(n, -1, -1):
    #
    #             if j == n:
    #                 ans = i == m
    #
    #             else:
    #                 first_match = i < m and p[j] in [s[i], '.']
    #
    #                 if j + 1 < n and p[j + 1] == '*':
    #                     ans = (dp[i][j + 2] or first_match and dp[i + 1][j])
    #                 else:
    #                     ans = (first_match and dp[i + 1][j + 1])
    #
    #             dp[i][j] = ans
    #
    #     return dp[0][0]

    """my initial attempt, wrong"""
    # def isMatch(self, s: str, p: str) -> bool:
    #     '''
    #     This answer is wrong, fail to consider '.*'
    #     :param s:
    #     :param p:
    #     :return:
    #     '''
    #     m, n = len(s), len(p)
    #     i, j = 0, 0
    #
    #     # loop
    #     while i < m and j < n:
    #
    #         # if doesn't match
    #         if p[j] != s[i]:
    #             if p[j] == '.':
    #                 pass
    #             elif p[j] == '*':
    #                 pass
    #             elif j + 1 < n:
    #                 if p[j + 1] == '*':
    #                     j = j + 2
    #                     continue
    #             else:
    #                 return False
    #
    #         # special situation: *, create substrings
    #         if p[j] == '*':
    #
    #             # case 1, .*
    #             if p[j - 1] == '.':
    #                 return True
    #
    #             # case 2, char + *
    #
    #             # i substring
    #             i_start = i - 1
    #             i_end = i - 1
    #             repeat_s_substring = ''
    #
    #             while i_end < m and s[i_end] == s[i_start]:
    #                 repeat_s_substring += s[i_end]
    #                 i_end += 1
    #
    #             # j substring
    #             j_start = j - 1
    #             j_end = j - 1
    #
    #             repeat_p_substring = ''
    #             while j_end < n and (p[j_end] == p[j_start] or p[j_end] == '*'):
    #                 repeat_p_substring += p[j_end]
    #                 j_end += 1
    #
    #             # replace i and j
    #             i = i_end
    #             j = j_end
    #
    #             continue
    #
    #         i += 1
    #         j += 1
    #
    #     if i == m and j == n:
    #         return True
    #     else:
    #         return False

    """my initial attempt wrong"""
    # def isMatch(self, s: str, p: str) -> bool:
    #     '''
    #     This is also a wrong answer. Wrong approach to recursive
    #     :param s:
    #     :param p:
    #     :return:
    #     '''
    #     # base case
    #     if len(p) <= 1:
    #
    #         # len(p) == 1
    #         if len(p) == 1:
    #             if p[0] == '.' and len(s) == 1:
    #                 return True
    #             elif s == p and len(s) == 1:
    #                 return True
    #             else:
    #                 return False
    #
    #         # len(p) == 0
    #         elif len(p) == 0:
    #             if s == p:
    #                 return True
    #             else:
    #                 return False
    #
    #     # recursive
    #     else:
    #
    #         if p[1] != '*':
    #
    #             # vanilla true:
    #             if s[0] == p[0]:
    #                 return self.isMatch(s[1:], p[1:])
    #
    #             # case '.'
    #             elif p[0] == '.':
    #                 return self.isMatch(s[1:], p[1:])
    #
    #             # vanilla false
    #             else:
    #                 return False
    #
    #         if p[1] == '*':
    #             # case 'char + *'
    #             if p[0] != '.':
    #
    #                 # if char matches
    #                 if p[0] == s[0]:
    #
    #                     i_end = 0
    #                     while i_end < len(s) and s[i_end] == s[0]:
    #                         i_end += 1
    #
    #                     return any([self.isMatch(s[i:], p[2:]) for i in range(i_end + 1)])
    #
    #                 # if char doesn't match
    #                 else:
    #                     return self.isMatch(s, p[2:])
    #
    #             # case '.*'
    #             elif p[0] == '.':
    #                 return any([self.isMatch(s[i:], p[2:]) for i in range(len(s) + 1)])

    """recursive ans"""
    # def isMatch(self, s: str, p: str) -> bool:
    #     if not p:
    #         return not s
    #
    #     first_match = bool(s) and p[0] in [s[0], '.']
    #
    #     if len(p) >= 2 and p[1] == '*':
    #         return (self.isMatch(s, p[2:]) or
    #                 first_match and self.isMatch(s[1:], p))
    #     else:
    #         return first_match and self.isMatch(s[1:], p[1:])







s = 'a'
p = 'a'
print(s, p, Solution().isMatch(s, p))

s = 'acd'
p = 'acde'
print(s, p, Solution().isMatch(s, p))

s = 'acd'
p = 'ac'
print(s, p, Solution().isMatch(s, p))

s = 'acccde'
p = 'ac*de'
print(s, p, Solution().isMatch(s, p))

s = 'acccde'
p = 'ac*cde'
print(s, p, Solution().isMatch(s, p))

s = 'accccde'
p = 'acc*cde'
print(s, p, Solution().isMatch(s, p))

s = 'acccde'
p = 'ac*cfe'
print(s, p, Solution().isMatch(s, p))

s = 'acccde'
p = 'ac*f*de'
print(s, p, Solution().isMatch(s, p))

s = 'acde'
p = 'a.de'
print(s, p, Solution().isMatch(s, p))

s = 'acdddef'
p = 'ac.*f'
print(s, p, Solution().isMatch(s, p))

s = 'acdddef'
p = 'ac.*fd'
print(s, p, Solution().isMatch(s, p))

s = 'acdddefdfdef'
p = 'ac.*fdef'
print(s, p, Solution().isMatch(s, p))

s = "ippi"
p = "ip*."
print(s, p, Solution().isMatch(s, p))

s = "aa"
p = "b*a"
print(s, p, Solution().isMatch(s, p))

s = 'a'
p = "c*a"
print(s, p, Solution().isMatch(s, p))
