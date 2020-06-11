class Solution:
    """my dfs sol, 1st attempt, modify from Q39"""
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans, candidates = [], list(range(1, 10))

        def dfs(target, idx, path, cur_sum, depth):  # add depth
            if depth > k:  # add depth
                return

            for i in range(idx, len(candidates)):
                if cur_sum + candidates[i] == target:
                    if depth == k:  # add depth
                        ans.append(path + [candidates[i]])
                    return
                elif cur_sum + candidates[i] < target:
                    dfs(target, i + 1, path + [candidates[i]], cur_sum + candidates[i], depth + 1)
                else:
                    return

        dfs(n, 0, [], 0, 1)
        return ans


