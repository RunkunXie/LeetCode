class Solution:
    #     def lengthOfLongestSubstring(self, s: str) -> int:

    #         if not s:
    #             return 0

    #         n = len(s)

    #         l, r = 0, 1

    #         result = 1
    #         crt = 1

    #         while r < n:

    #             r += 1

    #             if s[r-1] not in s[l:r]:
    #                 crt += 1
    #             else:
    #                 for i in range(l, r):
    #                     if s[r-1] not in s[i:r-1]:
    #                         l = i
    #                         crt = r - l
    #                         break

    #             if crt > result:
    #                 result += 1

    #         return result

    # same ideal, space for time
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






















