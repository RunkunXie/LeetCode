class Solution:
    """my dfs sol under hint, 1st attempt"""
    def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(i, j, board=[['.'] * n for _ in range(n)]):

            new_board = deepcopy(board)

            # put i-th queen
            new_board[i][j] = 'Q'
            if i == n - 1:
                ans.append(["".join(_).replace('x', '.') for _ in new_board])
                return

            # cross-out board area
            for y in range(n):
                if new_board[i][y] == '.':
                    new_board[i][y] = 'x'
            for x in range(n):
                if new_board[x][j] == '.':
                    new_board[x][j] = 'x'

            tmp = min(i, j)
            for k in range(-tmp, tmp + n):
                if 0 <= i + k < n and 0 <= j + k < n:
                    if new_board[i + k][j + k] == '.':
                        new_board[i + k][j + k] = 'x'
                else:
                    break

            tmp = min(n - i - 1, j)
            for k in range(-tmp, tmp + n):
                if 0 <= i - k < n and 0 <= j + k < n:
                    if new_board[i - k][j + k] == '.':
                        new_board[i - k][j + k] = 'x'
                else:
                    break

            # put i+1th queen
            for j in range(n):
                if new_board[i + 1][j] == '.':
                    dfs(i + 1, j, new_board)

        ans = []
        for j in range(n):
            dfs(0, j)

        return ans

    """my further modified sol after online hint, 1st attempt"""
    def solveNQueens(self, n):
        # write your code here

        def dfs(i=0, path=[]):

            # check terminal condition
            if i == n:
                ans.append(list(path))
                return

            for j in range(n):
                if (j not in cols and i + j not in diags and i - j not in off_diags):
                    # put i-th queen at i-th row, cross-out board area
                    path.append("." * j + "Q" + "." * (n - j - 1))
                    cols.add(j)
                    diags.add(i + j)
                    off_diags.add(i - j)

                    # put i+1th queen at i+1th row
                    dfs(i + 1, path)

                    # remove i-th queen from i-th row, reset board
                    path.pop()
                    cols.remove(j)
                    diags.remove(i + j)
                    off_diags.remove(i - j)

        ans, cols, diags, off_diags = [], set(), set(), set()
        dfs()

        return ans