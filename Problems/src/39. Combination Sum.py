from typing import List


class Solution:
    """"""

    """online backtrack sol"""
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()

        out = []
        sol = []

        def backtrack(val, pos):
            if val == 0:
                out.append(sol.copy())
                return
            else:
                for i in range(pos, len(nums)):
                    if val < nums[i]:
                        break
                    num = nums[i]
                    sol.append(num)
                    backtrack(val - num, i)
                    sol.pop()

        backtrack(target, 0)

        return out