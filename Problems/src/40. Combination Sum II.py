class Solution:
    """my dfs sol, 1st attempt, modified from Q39"""
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans, candidates, visited = [], sorted(candidates), [False] * len(candidates)

        def dfs(target, idx, path, cur_sum):

            for i in range(idx, len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1] and not visited[i - 1]:  # rule out repeat numbers
                    continue

                if cur_sum + candidates[i] == target:
                    ans.append(path + [candidates[i]])
                    return
                elif cur_sum + candidates[i] < target:
                    visited[i] = True
                    dfs(target, i + 1, path + [candidates[i]], cur_sum + candidates[i])
                    visited[i] = False
                else:
                    return

        dfs(target, 0, [], 0)
        return ans