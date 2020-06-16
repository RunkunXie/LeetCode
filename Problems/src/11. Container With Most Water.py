class Solution:

    """my sol, 2nd attempt"""
    def maxArea(self, height: List[int]) -> int:

        start, end, res = 0, len(height) - 1, 0

        while start < end:

            h = min(height[start], height[end])
            res = max(res, h * (end - start))

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return res

    def maxArea(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water