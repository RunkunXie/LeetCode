from typing import List


class Solution(object):
    """my sol under hint, further modified by append one zero, stack, time n"""
    class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:

            heights.append(0)
            n = len(heights)
            ans = 0

            s = [-1]

            for i, h in enumerate(heights):

                while s[-1] != -1 and heights[s[-1]] > h:
                    ans = max(ans, heights[s.pop()] * (i - s[-1] - 1))

                s.append(i)

            return ans

    """my sol under hint, stack, time n"""
    class Solution:
        def largestRectangleArea(self, heights: List[int]) -> int:

            s = [-1]
            n = len(heights)
            ans = 0

            for i, h in enumerate(heights):

                while s[-1] != -1 and heights[s[-1]] > h:
                    area = heights[s.pop()] * (i - s[-1] - 1)
                    ans = max(ans, area)

                s.append(i)

            while s[-1] != -1:
                area = heights[s.pop()] * (n - s[-1] - 1)
                ans = max(ans, area)

            return ans

    """ans, using stack, time n"""
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


print(Solution().largestRectangleArea([3, 2, 2, 3, 6, 1]))
