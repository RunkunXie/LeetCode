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

    def largestRectangleArea(self, heights):
        """
        O(n) using stack, another way, more concise, hard to understand
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):

            while stack[-1] != -1 and heights[i] <= heights[stack[-1]]:
                max_area = max(max_area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while stack[-1] != -1:
            max_area = max(max_area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        return max_area

    # def maximalRectangle(self, matrix) -> int:
    #     """
    #     DP method, O(M*N), directly use largestRectangleArea
    #     :param matrix: List[List[str]]
    #     :return: int
    #     """
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
    #                 dp[i][j] = dp[i][j - 1] + 1 if j else 1
    #
    #     for j in range(n):
    #         max_area = max(max_area,
    #                        self.largestRectangleArea([dp[i][j] for i in range(m)]))
    #
    #     return max_area

    def maximalRectangle(self, matrix) -> int:
        """
        DP method, O(M*N), modified dp and use largestRectangleArea.
        Previous dp, cal max width in a row.
        Current dp, cal width in column
        :param matrix: List[List[str]]
        :return: int
        """
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        max_area = 0
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                # for each row, update width from left to right
                dp[j] = dp[j - 1] + 1 if matrix[i][j] == '1' else 0

        max_area = max(max_area, self.largestRectangleArea(dp))

        return max_area
