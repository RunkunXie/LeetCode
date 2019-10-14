class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter

        n = len(s)
        t_dic = {char: 0 for char in t}
        t_require = Counter(t)

        l = 0  # left pointer, 0 to n-1
        r = -1  # right pointer, 0 to n-1

        min_len = float("inf")
        result = ""

        while True:

            # when current string contain t, move left
            if all([v >= t_require[k] for k, v in t_dic.items()]):

                # current length
                tmp_len = r + 1 - l
                if tmp_len < min_len:
                    min_len = tmp_len
                    result = s[l:r + 1]

                # move left, remove old left value
                if s[l] in t:
                    t_dic[s[l]] -= 1
                l += 1

            # else, move right
            else:

                # move right
                r += 1

                # check end
                if r >= n:
                    break

                # add new right value
                if s[r] in t:
                    t_dic[s[r]] += 1

        return result

# case 1
t = 'ABC'
s = "ADOBECODEBANC"
print(Solution().minWindow(s, t))

# case 2: char appear more than once in t
t = 'AABC'
s = "ADOBECODEBANC"
print(Solution().minWindow(s, t))
