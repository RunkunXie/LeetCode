class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s:
            return ''

        s = '.'.join(s)
        max_len = 1
        max_p = s[0]

        for c in range(len(s)):

            cur_p = ''
            cur_len = 0

            if s[c] is not '.':
                cur_p = s[c]
                cur_len = 1

            l = c - 1
            r = c + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                elif s[l] == s[r] and s[l] is not '.':
                    cur_p = s[l] + cur_p + s[r]
                    cur_len += 2
                l -= 1
                r += 1

            if cur_len > max_len:
                max_len = cur_len
                max_p = cur_p

        return max_p


print(Solution().longestPalindrome('abdde'))
print(Solution().longestPalindrome('babad'))
print(Solution().longestPalindrome('ccc'))
print(Solution().longestPalindrome('abcda'))