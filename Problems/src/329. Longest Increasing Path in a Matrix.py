class Solution:
    """my dp sol, 1st attempt, time n^2"""
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix or not matrix[0]:
            return 0

        direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        m, n = len(matrix), len(matrix[0])

        @lru_cache(None)
        def dfs(r, c):

            ans = 1

            for dr, dc in direction:

                new_r, new_c = r + dr, c + dc

                if 0 <= new_r < m and 0 <= new_c < n and matrix[r][c] < matrix[new_r][new_c]:
                    ans = max(ans, 1 + dfs(new_r, new_c))

            return ans

        return max([dfs(r, c) for r in range(m) for c in range(n)])

