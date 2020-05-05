from typing import List


class Solution:

    """online sol"""
    def letterCombinations(self, digits: str) -> List[str]:

        phone = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs",
                 '8': "tuv", '9': "wxyz"}

        cmb = [''] if digits else []

        for d in digits:
            cmb = [p + q for p in cmb for q in phone[d]]

        return cmb

    """online sol, backtrack"""
    # def letterCombinations(self, digits: str) -> List[str]:
    #     phone = {'2': ['a', 'b', 'c'],
    #              '3': ['d', 'e', 'f'],
    #              '4': ['g', 'h', 'i'],
    #              '5': ['j', 'k', 'l'],
    #              '6': ['m', 'n', 'o'],
    #              '7': ['p', 'q', 'r', 's'],
    #              '8': ['t', 'u', 'v'],
    #              '9': ['w', 'x', 'y', 'z']}
    #
    #     if not digits:
    #         return []
    #
    #     def genComb(l, digits):
    #         if not digits:
    #             return l
    #
    #         ans = []
    #         for c1 in l:
    #             for c2 in phone[digits[0]]:
    #                 ans.append(c1 + c2)
    #
    #         return genComb(ans, digits[1:])
    #
    #     return genComb(phone[digits[0]], digits[1:])


print(Solution().letterCombinations('234'))
