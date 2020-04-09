import itertools


class Solution:
    """"""

    """my sol, time n, space 1"""
    # def backspaceCompare(self, S: str, T: str) -> bool:
    #
    #     i, j = len(S), len(T)
    #
    #     while i >= 0 and j >= 0:
    #
    #         i -= 1
    #         j -= 1
    #
    #         count_i = 0
    #         count_j = 0
    #
    #         while i >= 0 and (S[i] == '#' or count_i > 0):
    #
    #             if S[i] == '#':
    #                 count_i += 1
    #             elif count_i > 0:
    #                 count_i -= 1
    #             i -= 1
    #
    #         while j >= 0 and (T[j] == '#' or count_j > 0):
    #
    #             if T[j] == '#':
    #                 count_j += 1
    #             elif count_j > 0:
    #                 count_j -= 1
    #             j -= 1
    #
    #         print(i, S[i], j, T[j])
    #         if i == -1 ^ j == -1:
    #             return False
    #         elif i == -1 and j == -1:
    #             return True
    #         elif S[i] != T[j]:
    #             return False

    """beautiful answer, time n, space 1"""
    def backspaceCompare(self, S, T):
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))
