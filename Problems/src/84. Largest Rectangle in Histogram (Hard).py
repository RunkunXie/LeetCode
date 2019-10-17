class Solution(object):
    # def largestRectangleArea(self, heights):
    #     """
    #     O(n) using stack, easy to understand version
    #     :type heights: List[int]
    #     :rtype: int
    #     """
    #     # for every bar, calc the area which uses this bar as the lowest bar
    #     # therefore we need to find the first lower bar towards the left and the
    #     # first lower bar towards the right
    #     # hence, we need a stack to keep stacking the higher bars
    #     # when a lower bar appears, thats the first lower bar towards the right
    #     # and the first lower bar towards the left will be the next bar in the stack
    #     stack = []
    #     max_area = 0
    #     for i in range(len(heights)):
    #         if not stack:
    #             stack.append(i)
    #         else:
    #             # if height not decreasing, just stack
    #             if heights[i] >= heights[stack[-1]]:
    #                 stack.append(i)
    #                 continue
    #             while stack and heights[i] < heights[stack[-1]]:
    #                 # for the bar on top of the stack
    #                 # we found the first lower bar towards the right
    #                 this_bar = stack.pop()
    #                 right_index = i
    #                 left_index = stack[
    #                     -1] if stack else -1  # no lower towards the left, so make it left of the leftmost, which makes it -1
    #                 area = heights[this_bar] * (right_index - left_index - 1)
    #                 max_area = max(area, max_area)
    #             stack.append(i)
    #     while stack:
    #         this_bar = stack.pop()
    #         right_index = len(
    #             heights)  # no lower towards the right, so make it right of the rightmost, which makes it len(heights)
    #         left_index = stack[-1] if stack else -1
    #         area = heights[this_bar] * (right_index - left_index - 1)
    #         max_area = max(area, max_area)
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


print(Solution().largestRectangleArea([3, 2, 2, 3, 6, 1]))
