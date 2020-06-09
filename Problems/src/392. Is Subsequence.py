class Solution:
    """
    my dp sol, similar to greedy, time len(t),
    if many s, time n*len(t)
    """
    def isSubsequence(self, s: str, t: str) -> bool:

        @lru_cache(None)
        def dp(i, j):

            if i == -1:
                return True

            if j == -1:
                return False

            if s[i] == t[j]:
                ans = dp(i - 1, j - 1)
            else:
                ans = dp(i, j - 1)

            return ans

        return dp(len(s) - 1, len(t) - 1)

    """
    followup: many s?
    ans, use dict, time len(t) + len(s)*log(len(t))
    if many s, time len(t) + n*len(s)*log(len(t))
    """
    def isSubsequence(self, s: str, t: str) -> bool:

        letter_indices_table = defaultdict(list)
        for index, letter in enumerate(t):
            letter_indices_table[letter].append(index)

        curr_match_index = -1
        for letter in s:
            if letter not in letter_indices_table:
                return False  # no match at all, early exit

            # greedy match with binary search
            indices_list = letter_indices_table[letter]
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False # no suitable match found, early exist

        return True