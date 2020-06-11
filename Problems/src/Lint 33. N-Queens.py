from copy import deepcopy


class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    """my sol after online hint, 1st attempt"""
    def solveNQueens(self, n):
        # write your code here

        def dfs(i, j, path):

            # put i-th queen at i-th row, cross-out board area
            path.append("." * j + "Q" + "." * (n - j - 1))

            # check terminal condition
            if i == n - 1:
                ans.append(list(path))
                path.pop()
                return

            cols.add(j)
            diags.add(i + j)
            off_diags.add(i - j)

            # put i+1th queen at i+1th row
            next_i = i + 1
            for next_j in range(n):
                if (next_j not in cols and
                        next_i + next_j not in diags and
                        next_i - next_j not in off_diags):
                    dfs(next_i, next_j, path)

            # remove i-th queen from i-th row, reset board
            path.pop()
            cols.remove(j)
            diags.remove(i + j)
            off_diags.remove(i - j)

        ans, cols, diags, off_diags = [], set(), set(), set()
        for j in range(n):
            dfs(0, j, [])

        return ans

    """my further modified sol, 1st attempt"""
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