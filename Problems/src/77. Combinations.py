class Solution:

    """my sol, 1st attempt"""
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations(list(range(1, n + 1)), k)

    """my dfs sol, 1st attempt"""
    def combine(self, n: int, k: int) -> List[List[int]]:

        candidates = list(range(1, n + 1))
        ans = []

        def dfs(idx, path, depth):

            for i in range(idx, n):
                if depth == k:
                    ans.append(path + [candidates[i]])
                elif depth < k:
                    dfs(i + 1, path + [candidates[i]], depth + 1)

        dfs(0, [], 1)
        return ans