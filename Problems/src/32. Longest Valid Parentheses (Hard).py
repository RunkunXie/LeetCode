class Solution:
    """Solution without extra space, O(n)"""
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        max_len = 0

        # left to right
        count_l = 0
        count_r = 0

        for i, v in enumerate(s):

            # count left and right
            if v == '(':
                count_l += 1
            else:
                count_r += 1

            # judge new situation
            tmp_len = 0
            if count_l == count_r:
                tmp_len = 2 * count_r
            elif count_l < count_r:
                count_l = 0
                count_r = 0

            # replace max
            if tmp_len > max_len:
                max_len = tmp_len

        # right to left
        count_l = 0
        count_r = 0

        for i, v in enumerate(reversed(s)):

            # count left and right
            if v == ')':
                count_l += 1
            else:
                count_r += 1

            # judge new situation
            tmp_len = 0
            if count_l == count_r:
                tmp_len = 2 * count_r
            elif count_l < count_r:
                count_l = 0
                count_r = 0

            # replace max
            if tmp_len > max_len:
                max_len = tmp_len

        # return
        return max_len

    """DP solution with stack"""
    def longestValidParentheses(self, s: str) -> int:

        # dp[i + 1] is the longest valid for s[:i + 1], i = 0 to n-1
        dp = [0] * (len(s) + 1)
        stack = []

        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop()
                    dp[i + 1] = dp[p] + (i - p + 1)

        return max(dp)


print(Solution().longestValidParentheses('(()(())'), 6)
print(Solution().longestValidParentheses(')('), 0)
print(Solution().longestValidParentheses('()()'), 4)
print(Solution().longestValidParentheses('('), 0)
print(Solution().longestValidParentheses('()(()'), 2)
