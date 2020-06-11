from typing import List


class Solution:
    """"""

    """my dfs sol, 2nd attempt"""
    def combinationSum(self, candidates, target):
        # write your code here

        ans, candidates = [], sorted(list(set(candidates)))

        def dfs(target, idx, path, cur_sum):

            for i in range(idx, len(candidates)):
                if cur_sum + candidates[i] == target:
                    ans.append(path + [candidates[i]])
                    return
                elif cur_sum + candidates[i] < target:
                    dfs(target, i, path + [candidates[i]], cur_sum + candidates[i])
                else:
                    return

        dfs(target, 0, [], 0)
        return ans

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