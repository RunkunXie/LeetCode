class Solution:
    """my sol, directly modify from Q51"""
    def totalNQueens(self, n: int) -> int:

        def dfs(i=0):

            # check terminal condition
            if i == n:
                self.ans += 1
                return

            for j in range(n):
                if (j not in cols and i + j not in diags and i - j not in off_diags):
                    # put i-th queen at i-th row, cross-out board area
                    cols.add(j)
                    diags.add(i + j)
                    off_diags.add(i - j)

                    # put i+1th queen at i+1th row
                    dfs(i + 1)

                    # remove i-th queen from i-th row, reset board
                    cols.remove(j)
                    diags.remove(i + j)
                    off_diags.remove(i - j)

        self.ans, cols, diags, off_diags = 0, set(), set(), set()
        dfs()

        return self.ans