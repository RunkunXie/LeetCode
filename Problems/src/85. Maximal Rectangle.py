class Solution:
    # def maximalRectangle(self, matrix) -> int:
    #     """
    #     DP method, O(M*N^2)
    #     :param matrix: List[List[str]]
    #     :return: int
    #     """
    #
    #     if not matrix:
    #         return 0
    #
    #     m, n = len(matrix), len(matrix[0])
    #
    #     dp = [[0] * n for _ in range(m)]
    #
    #     max_area = 0
    #
    #     for i in range(m):
    #         for j in range(n):
    #
    #             if matrix[i][j] == '0':
    #                 continue
    #
    #             else:
    #                 # for each row, update width from left to right
    #                 width = dp[i][j] = dp[i][j-1] + 1 if j else 1
    #
    #                 # then search upwards
    #                 for k in range(i, -1, -1):
    #                     width = min(width, dp[k][j])
    #                     max_area = max(max_area, width * (i - k + 1))
    #
    #     return max_area

    @staticmethod
    def largestRectangleArea(heights):

        heights.append(0)
        ans = 0

        s = [-1]
        for i, h in enumerate(heights):
            while s[-1] != -1 and heights[s[-1]] > h:
                ans = max(ans, heights[s.pop()] * (i - s[-1] - 1))
            s.append(i)

        return ans

    """
    DP method, O(M*N), directly use largestRectangleArea
    :param matrix: List[List[str]]
    :return: int
    """
    def maximalRectangle(self, matrix) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_area = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i - 1][j] + 1 if i else 1

            max_area = max(max_area, self.largestRectangleArea(dp[i]))

        return max_area

    """
    DP method, O(M*N), modified dp and use largestRectangleArea.
    :param matrix: List[List[str]]
    :return: int
    """
    def maximalRectangle(self, matrix) -> int:

        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        max_area = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area
