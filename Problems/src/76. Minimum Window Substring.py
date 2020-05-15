from collections import Counter


class Solution:
    """"""

    """my sol"""
    # def minWindow(self, s: str, t: str) -> str:
    #
    #     n = len(s)
    #     t_dic = {char: 0 for char in t}
    #     t_require = Counter(t)
    #
    #     l = 0  # left pointer, 0 to n-1
    #     r = -1  # right pointer, 0 to n-1
    #
    #     min_len = float("inf")
    #     result = ""
    #
    #     while True:
    #
    #         # when current string contain t, move left
    #         if all([v >= t_require[k] for k, v in t_dic.items()]):
    #
    #             # current length
    #             tmp_len = r + 1 - l
    #             if tmp_len < min_len:
    #                 min_len = tmp_len
    #                 result = s[l:r + 1]
    #
    #             # move left, remove old left value
    #             if s[l] in t:
    #                 t_dic[s[l]] -= 1
    #             l += 1
    #
    #         # else, move right
    #         else:
    #
    #             # move right
    #             r += 1
    #
    #             # check end
    #             if r >= n:
    #                 break
    #
    #             # add new right value
    #             if s[r] in t:
    #                 t_dic[s[r]] += 1
    #
    #     return result

    """ans, Sliding Window"""
    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)

        # left and right pointer
        l, r = 0, 0

        # formed is used to keep track of how many unique characters in t are present in the current window in its
        # desired frequency. e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed
        # would be = 3 when all these conditions are met.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):

            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # If the frequency of the current character added equals to the desired count in t then increment the
            # formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                l += 1

                # Keep expanding the window once we are done contracting.
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

    """ans, Optimized Sliding Window, time s+t"""

    def minWindow(self, s: str, t: str) -> str:

        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))

        l, r = 0, 0
        formed = 0
        window_counts = {}

        ans = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1

            if window_counts[character] == dict_t[character]:
                formed += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]

                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)

                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


# case 1
t = 'ABC'
s = "ADOBECODEBANC"
print(Solution().minWindow(s, t))

# case 2: char appear more than once in t
t = 'AABC'
s = "ADOBECODEBANC"
print(Solution().minWindow(s, t))
