from typing import List


class Solution:
    """"""

    """my 2pointer sol, 2nd attempt, time n"""
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        start, end, ans = 0, len(height) - 1, 0
        h1, h2 = height[start], height[end]

        while start < end:

            if height[start] < height[end]:

                if height[start] < h1:
                    ans += h1 - height[start]
                start += 1
                h1 = max(h1, height[start])

            else:

                if height[end] < h2:
                    ans += h2 - height[end]
                end -= 1
                h2 = max(h2, height[end])

        return ans

    """my sol, time n^2"""
    # def trap(self, height: List[int]) -> int:
    #
    #     if not height:
    #         return 0
    #
    #     max_h = max(height)
    #     ans = 0
    #     l, r = 0, len(height) - 1
    #
    #     for h in range(1, max_h + 1):
    #
    #         while height[l] < h:
    #             l += 1
    #
    #         while height[r] < h:
    #             r -= 1
    #
    #         if l == r:
    #             break
    #
    #         for i in range(l, r + 1):
    #             if height[i] < h:
    #                 height[i] += 1
    #                 ans += 1
    #
    #     return ans

    """my sol after hint, use two pointers, time n"""
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        ans = 0
        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]

        while l < r:

            if l_max <= r_max:
                l += 1
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    ans += min(l_max, r_max) - height[l]

            elif l_max >= r_max:
                r -= 1
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    ans += min(l_max, r_max) - height[r]

        return ans

    """ans 2, dp method, cal l_max and r_max using two loop"""
    """ans 3, using stack"""


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
