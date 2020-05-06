class Solution:
    """my first attemp, not good way for partition"""
    # def searchMatrix(self, matrix, target):
    #     """
    #     :type matrix: List[List[int]]
    #     :type target: int
    #     :rtype: bool
    #     """
    #
    #     m, n = len(matrix), len(matrix[0])
    #
    #     def f(x, y, h, w, target):
    #
    #         if h == 0 and w == 0:
    #             return matrix[x][y] == target
    #         elif h == 0:
    #             return
    #
    #         mid_h = int(h / 2)
    #         mid_w = int(w / 2)
    #
    #         if matrix[x + mid_h][y + mid_w] == target:
    #             return True
    #
    #         elif matrix[x + mid_h][y + mid_w] < target:
    #             return f(x, y, mid_h, mid_w) and f(
    #                 x + mid_h + 1, y, h - mid_h - 1, mid_w - 1) and f(
    #                 x, y + mid_w + 1, mid_h - 1, w - mid_w - 1)
    #
    #         elif elif matrix[x + mid_h][y + mid_w] > target:
    #
    #     return f(0, 0, m - 1, n - 1)

    """ans, divide-conquer, time nlogn"""
    # def searchMatrix(self, matrix, target):
    #     # an empty matrix obviously does not contain `target`
    #     if not matrix:
    #         return False
    #
    #     def search_rec(left, up, right, down):
    #         # this submatrix has no height or no width.
    #         if left > right or up > down:
    #             return False
    #         # `target` is already larger than the largest element or smaller
    #         # than the smallest element in this submatrix.
    #         elif target < matrix[up][left] or target > matrix[down][right]:
    #             return False
    #
    #         mid = left + (right - left) // 2
    #
    #         # Locate `row` such that matrix[row-1][mid] < target < matrix[row][mid]
    #         row = up
    #         while row <= down and matrix[row][mid] <= target:
    #             if matrix[row][mid] == target:
    #                 return True
    #             row += 1
    #
    #         return search_rec(left, row, mid - 1, down) or search_rec(mid + 1, up, right, row - 1)
    #
    #     return search_rec(0, 0, len(matrix[0]) - 1, len(matrix) - 1)

    """ans, two pointer, optimal, time m + n"""
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False