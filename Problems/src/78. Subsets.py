from typing import List


class Solution:
    """"""

    """my sol, 2nd attempt"""
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        sub = self.subsets(nums[1:])
        return [[nums[0]] + s for s in sub] + sub

    """recursion answer, time n * 2**n"""
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output

    """binary solution"""
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     n = len(nums)
    #     output = []
    #
    #     for i in range(2 ** n, 2 ** (n + 1)):
    #         # generate bitmask, from 0..00 to 1..11
    #         bitmask = bin(i)[3:]
    #
    #         # append subset corresponding to that bitmask
    #         output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    #
    #     return output