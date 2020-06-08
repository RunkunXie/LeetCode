class Solution:
    """my dfs sol, 1st attempt, time mn"""
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'B'
                list(map(dfs, (i - 1, i + 1, i, i), (j, j, j - 1, j + 1)))

        # mark border by B
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # replace O by X AND B by O
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'
