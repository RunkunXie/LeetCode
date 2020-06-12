class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        d1, d2 = {}, {}
        m, n = len(pattern), len(str)
        self.ans = False

        def dfs(i=0, j=0):

            if i == m and j == n:
                self.ans = True
                return

            elif i == m or j == n:
                return

            p = pattern[i]

            if p in d1:
                s = d1[p]
                if j + len(s) <= n and str[j:j + len(s)] == s:
                    dfs(i + 1, j + len(s))

            else:
                for end_j in range(j + 1, n + 1):
                    s = str[j:end_j]
                    if s not in d2:
                        d1[p] = s
                        d2[s] = p
                        dfs(i + 1, end_j)
                        d1.pop(p)
                        d2.pop(s)

        dfs()
        return self.ans

    """my dfs sol, 1st attempt 2nd try, return True when find"""
    def wordPatternMatch(self, pattern, str):
        # write your code here

        d1, d2 = {}, {}
        m, n = len(pattern), len(str)

        def dfs(i=0, j=0):

            # terminate condition: both reach end, True
            if i == m and j == n:
                return True

            # terminate condition: one reach end, False
            elif i == m or j == n:
                return False

            # not terminate: process current pattern – p
            p = pattern[i]

            # if p appeared before
            if p in d1:
                s = d1[p]
                return str[j:].startswith(s) and dfs(i + 1, j + len(s))

            # if p not appeared before, find possible s in str start from i + 1 for p to match
            else:
                for end_j in range(j + 1, n + 1):
                    s = str[j:end_j]

                    # if s not appeared before as well, run dfs
                    if s not in d2:
                        d1[p] = s
                        d2[s] = p
                        if dfs(i + 1, end_j):
                            return True
                        d1.pop(p)
                        d2.pop(s)
                return False

        return dfs()
