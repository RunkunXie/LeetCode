class Solution:
    """my sol, time n*m*4^L"""
    def exist(self, board: List[List[str]], word: str) -> bool:

        length = len(word)
        m, n = len(board), len(board[0])
        used = set()
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        self.ans = False

        def dfs(i, j, x, length, used):

            if not (0 <= i < m and 0 <= j < n) or (i, j) in used:
                return

            if board[i][j] == word[x]:

                if x == length - 1:
                    self.ans = True
                    return

                else:
                    used.add((i, j))
                    for di, dj in direction:
                        dfs(i + di, j + dj, x + 1, length, used)
                    used.remove((i, j))

        for i in range(m):
            for j in range(n):
                dfs(i, j, 0, length, used)

        return self.ans

