from collections import deque

#%%
class Solution:
    """"""
    """sorting takes nlogn time, n space"""
    # def findUnsortedSubarray(self, nums) -> int:
    #
    #     nums_sort = sorted(nums)
    #
    #     l = None
    #     for i in range(len(nums)):
    #         if nums[i] != nums_sort[i]:
    #             l = i
    #             break
    #
    #     for j in range(len(nums) - 1, -1, -1):
    #         if nums[j] != nums_sort[j]:
    #             r = j
    #             break
    #
    #     if l is not None:
    #         return r - l + 1
    #
    #     return 0

    """ find OHLC, O(N) time, O(1) space"""
    # def findUnsortedSubarray(self, nums) -> int:
    #     p_l = p_r = None
    #     num_low = num_high = None
    #
    #     for i in range(1, len(nums)):
    #         if nums[i] < nums[i - 1] and p_l is None:
    #             p_l = i
    #             num_low = nums[i]
    #         if num_low is not None:
    #             if nums[i] < num_low:
    #                 num_low = nums[i]
    #
    #     for j in range(len(nums) - 2, -1, -1):
    #         if nums[j] > nums[j + 1] and p_r is None:
    #             p_r = j
    #             num_high = nums[j]
    #         if num_high is not None:
    #             if nums[j] > num_high:
    #                 num_high = nums[j]
    #
    #     if p_l is not None:
    #
    #         p_start = p_l
    #         while p_start >= 0:
    #             p_start -= 1
    #             if p_start == -1:
    #                 break
    #             if nums[p_start] <= num_low:
    #                 break
    #
    #         p_end = p_r
    #         while p_end <= len(nums) - 1:
    #             p_end += 1
    #             if p_end == len(nums):
    #                 break
    #             if nums[p_end] >= num_high:
    #                 break
    #
    #         return p_end - p_start - 1
    #
    #     return 0

    """find OHLC using STACK, n time, n space"""
    def findUnsortedSubarray(self, nums) -> int:

        stack = []
        min_len_l = None
        min_l = None
        for num in nums:
            if not stack:
                stack.append(num)
            else:
                if num >= stack[-1]:
                    stack.append(num)
                else:
                    if min_l is None or num < min_l:
                        while stack and num < stack[-1]:
                            stack.pop()
                        min_len_l = len(stack)
                        min_l = num
                    stack.append(num)

        stack = []
        min_len_r = None
        max_r = None
        for num in reversed(nums):
            if not stack:
                stack.append(num)
            else:
                if num <= stack[-1]:
                    stack.append(num)
                else:
                    if max_r is None or num > max_r:
                        while stack and num > stack[-1]:
                            stack.pop()
                        min_len_r = len(stack)
                        max_r = num
                    stack.append(num)

        if min_len_l is not None:
            return len(nums) - min_len_l - min_len_r

        return 0


print(Solution().findUnsortedSubarray([2,6,4,8,10,9,15]), 5)
print(Solution().findUnsortedSubarray([2,1]), 2)