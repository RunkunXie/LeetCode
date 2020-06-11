"""
LC Q39
"""

class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """

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