from typing import List


class Solution:
    """"""

    """online sol, time n, space n"""
    # def findMaxLength(self, nums: List[int]) -> int:
    #     c,d,m = 0,{0:0},0
    #     for i,v in enumerate(nums):
    #         c += 2*v -1
    #         if c in d:
    #             m = max(m,i+1-d[c])
    #         else:
    #             d[c] = i+1
    #     return m

    """my sol - 2nd attempt"""
    def findMaxLength(self, nums: List[int]) -> int:

        max_count = count = 0
        prev_count = {0: -1}

        for i, num in enumerate(nums):

            # current level
            count = count + 1 if num else count - 1

            # check if equal to previous level: if True, Contiguous Array exist
            if count not in prev_count:
                prev_count[count] = i

            # add new Contiguous Array length
            else:
                max_count = max(i - prev_count[count], max_count)

        return max_count