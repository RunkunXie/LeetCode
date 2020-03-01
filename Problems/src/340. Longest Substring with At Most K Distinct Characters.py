from collections import OrderedDict


class Solution:
    # def lengthOfLongestSubstringKDistinct(self, s: str, k:int) -> int:
    #     """
    #     O(kN), dict method 1, similar to hashmap
    #     :param s:
    #     :param k:
    #     :return:
    #     """
    #     if not s or not k:
    #         return 0
    #
    #     # store current index, and max length
    #     cur_dic = {}
    #     max_len = 0
    #
    #     # loop
    #     tmp_len = 0
    #     left = 0
    #     for i in range(len(s)):
    #
    #         # new element
    #         if s[i] in cur_dic.keys():
    #             cur_dic[s[i]] += 1
    #         else:
    #             cur_dic[s[i]] = 1
    #
    #         # when #(distinct element) > k
    #         while len(cur_dic.keys()) > k and left < i:
    #
    #             if cur_dic[s[left]] == 1:
    #                 cur_dic.pop(s[left])
    #             else:
    #                 cur_dic[s[left]] -= 1
    #
    #             left += 1
    #
    #         # update max length
    #         max_len = max(max_len, i - left + 1)
    #
    #     return max_len

    # def lengthOfLongestSubstringKDistinct(self, s: str, k:int) -> int:
    #     """
    #     O(kN), dict method 2, similar to hashmap
    #     instead of store number of char in dict values, we store the leftmost index of that char
    #     :param s:
    #     :param k:
    #     :return:
    #     """
    #     if not s or not k:
    #         return 0
    #
    #     # store current index, and max length
    #     cur_dic = {}
    #     max_len = 0
    #
    #     # loop
    #     left = 0
    #     for i in range(len(s)):
    #
    #         # new element
    #         cur_dic[s[i]] = i
    #
    #         # when #(distinct element) > k
    #         if len(cur_dic.keys()) == k + 1:
    #
    #             del_idx = min(cur_dic.values())
    #
    #             cur_dic.pop(s[del_idx])
    #
    #             left = del_idx + 1
    #
    #         # update max length
    #         max_len = max(max_len, i - left + 1)
    #
    #     return max_len

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """
        O(kN), ordered dict method
        instead of store number of char in dict values, we store the leftmost index of that char
        :param s:
        :param k:
        :return:
        """
        if not s or not k:
            return 0

        # store current index, and max length
        cur_dic = OrderedDict()
        max_len = 0

        # loop
        left = 0
        for i in range(len(s)):

            # new element
            if s[i] in cur_dic.keys():
                cur_dic.pop(s[i])

            cur_dic[s[i]] = i

            # when #(distinct element) > k
            if len(cur_dic.keys()) == k + 1:

                _, del_idx = cur_dic.popitem(last=False)  # if use dict, next(iter(cur_dic.items()))

                left = del_idx + 1

            # update max length
            max_len = max(max_len, i - left + 1)

        return max_len


print(Solution().lengthOfLongestSubstringKDistinct("eceba", 2), 3)
print(Solution().lengthOfLongestSubstringKDistinct("aa", 1), 2)
print(Solution().lengthOfLongestSubstringKDistinct("abaccc", 2), 4)
