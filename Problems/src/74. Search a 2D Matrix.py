class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        start = 0
        end = m * n - 1

        while start <= end:
            mid = start + (end - start) // 2
            i_row, i_col = divmod(mid, n)
            if matrix[i_row][i_col] == target:
                return True
            elif matrix[i_row][i_col] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False