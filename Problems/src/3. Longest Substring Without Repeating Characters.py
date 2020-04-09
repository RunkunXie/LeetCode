from collections import deque


class Solution:
    """"""

    """my sol, naive iteration, time n^2"""
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        n = len(s)

        l, r = 0, 1

        result = 1
        crt = 1

        while r < n:

            r += 1

            if s[r-1] not in s[l:r]:
                crt += 1
            else:
                for i in range(l, r):
                    if s[r-1] not in s[i:r-1]:
                        l = i
                        crt = r - l
                        break

            if crt > result:
                result += 1

        return result

    """my sol, Sliding Window, using HashSet, time 2n"""
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s is None:
            return None

        ans = deque([])
        ans_set = set()
        length = 0
        max_len = 0

        for x in s:
            if x not in ans_set:
                ans.append(x)
                ans_set.add(x)
                length += 1
                if length > max_len:
                    max_len = length
            else:
                while ans[0] is not x:
                    ans_set.discard(ans.popleft())
                    length -= 1

                ans.popleft()
                ans.append(x)

        return max_len

    """my sol, Sliding Window Optimized, use dict to index, time n, space n"""
    def lengthOfLongestSubstring(self, s: str) -> int:

        dic = {}
        result = 0
        crt_max = 0
        start_i = 0

        for end_i, c in enumerate(s):

            if c in dic and dic[c] >= start_i:
                start_i = dic[c] + 1
                crt_max = end_i - start_i + 1
            else:
                crt_max += 1

            dic[c] = end_i

            if result < crt_max:
                result = crt_max

        return result






















