from typing import List
from collections import deque, defaultdict
from itertools import chain


class Solution:
    """my sol at contest"""
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        ans = []

        n = len(nums)
        num_len = [len(num) for num in nums]
        num_row = max([num_len[i] + i for i in range(n)])

        i_range = deque([])

        for r in range(num_row):

            if r < n:
                i_range.appendleft(r)

            remove_i = []

            for i in i_range:

                if r < i:
                    continue

                j = r - i
                if j < num_len[i]:
                    ans.append(nums[i][j])
                else:
                    remove_i.append(i)

            while remove_i:
                i_range.remove(remove_i.pop())

        return ans

    """my sol after hint, using dict"""
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        max_row = 0
        row_dict = defaultdict(list)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(nums[i])):
                row_dict[i + j].append(nums[i][j])
            max_row = max(max_row, len(nums[i]) + i)

        ans = []
        for row in range(max_row):
            ans += row_dict[row]

        return ans

    """online sol using dict, cleaner"""
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

        diagonals = defaultdict(lambda: deque())

        for i, line in enumerate(nums):
            for j in range(len(line)):
                diagonals[i + j].appendleft(line[j])

        return list(chain(*diagonals.values()))
        # chain(*iterables) or chain.from_iterable(iterables)
        # return list(chain.from_iterable(diagonals.values()))