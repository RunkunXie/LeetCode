from collections import deque
from typing import List


class MonotonicQueue:
    def __init__(self):
        self.dq = deque([])

    def push(self, item):
        while self.dq and item > self.dq[-1]:
            self.dq.pop()

        self.dq.append(item)

    def pop(self, item):
        if item == self.dq[0]:
            self.dq.popleft()

    def max(self):
        return self.dq[0]


class Solution:
    """"""

    """my deque sol under hint, time n (140ms beat 99%), best sol"""
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        if n == k:
            return [max(nums)]

        l = deque([])
        ans = []

        for i in range(k - 1):

            # push
            while l:
                if l[-1] < nums[i]:
                    l.pop()
                else:
                    break
            l.append(nums[i])

        for i in range(k - 1, n):

            # push
            while l:
                if l[-1] < nums[i]:
                    l.pop()
                else:
                    break
            l.append(nums[i])

            # ans
            ans.append(l[0])

            # pop
            if l[0] == nums[i - k + 1]:
                l.popleft()

        return ans

    """online sol using MonotonicQueue"""
    class Solution:
        def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            if not nums or not k:
                return []

            monotonic_q = MonotonicQueue()

            for i in range(k - 1):
                monotonic_q.push(nums[i])

            result = []

            for i in range(k - 1, len(nums)):
                monotonic_q.push(nums[i])
                result.append(monotonic_q.max())
                monotonic_q.pop(nums[i - k + 1])

            return result

    """O(kN), brute force"""
    # def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
    #     if not nums:
    #         return None
    #
    #     max_w = []
    #
    #     for i in range(len(nums) - k + 1):
    #         max_w.append(max(nums[i:i + k]))
    #
    #     return max_w

    """O(logk*N), heap"""
    # def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
    #
    #     if not nums:
    #         return None
    #
    #     max_element = []
    #     cur_w = []
    #
    #     for i, v in enumerate(nums):
    #
    #         heappush(cur_w, - v)
    #
    #         if i >= k - 1:
    #             heapify(cur_w)
    #             cur_max = - heappop(cur_w)
    #             max_element.append(cur_max)
    #             heappush(cur_w, - cur_max)
    #             cur_w.remove(- nums[i - k + 1])
    #
    #     return max_element

    """O(N), use list as deque"""
    # def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
    #
    #     # special case 1
    #     if not nums:
    #         return None
    #
    #     # special case 2
    #     if k == 1:
    #         return nums
    #
    #     # store max element, and current index
    #     max_element = []
    #     cur_w_idx = []
    #
    #     # clear queue
    #     def clear_que():
    #         if cur_w_idx and cur_w_idx[0] == i - k:
    #             cur_w_idx.pop(0)
    #
    #         while cur_w_idx and nums[cur_w_idx[-1]] < nums[i]:
    #             cur_w_idx.pop()
    #
    #     # first k element
    #     max_num = nums[0]
    #     for i in range(k):
    #
    #         clear_que()
    #
    #         cur_w_idx.append(i)
    #
    #         if nums[i] > max_num:
    #             max_num = nums[i]
    #
    #     max_element.append(max_num)
    #
    #     # k + 1 to last element
    #     for i in range(k, len(nums)):
    #         clear_que()
    #
    #         cur_w_idx.append(i)
    #
    #         max_element.append(nums[cur_w_idx[0]])
    #
    #     return max_element

    """O(N), deque, intuitive"""
    # def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
    #
    #     # special case 1
    #     if not nums:
    #         return None
    #
    #     # special case 2
    #     if k == 1:
    #         return nums
    #
    #     # store max element, and current index
    #     max_element = []
    #     cur_w_idx = deque()
    #
    #     # clear queue
    #     def clear_que():
    #         if cur_w_idx and cur_w_idx[0] == i - k:
    #             cur_w_idx.popleft()
    #
    #         while cur_w_idx and nums[cur_w_idx[-1]] < nums[i]:
    #             cur_w_idx.pop()
    #
    #     # first k element
    #     max_num = nums[0]
    #     for i in range(k):
    #
    #         clear_que()
    #
    #         cur_w_idx.append(i)
    #
    #         if nums[i] > max_num:
    #             max_num = nums[i]
    #
    #     max_element.append(max_num)
    #
    #     # k + 1 to last element
    #     for i in range(k, len(nums)):
    #         clear_que()
    #
    #         cur_w_idx.append(i)
    #
    #         max_element.append(nums[cur_w_idx[0]])
    #
    #     return max_element

    """O(N), DP"""
    # def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
    #
    #     # special case 1
    #     if not nums:
    #         return None
    #
    #     # special case 2
    #     if k == 1:
    #         return nums
    #
    #     # store max element
    #     left = []
    #     right = []
    #     max_element = []
    #
    #     # left[i]: maximum of block start to nums[i]
    #     for i, v in enumerate(nums):
    #
    #         if i % k == 0:
    #             block_max = v
    #             left.append(v)
    #         else:
    #             if v > block_max:
    #                 left.append(v)
    #                 block_max = v
    #             else:
    #                 left.append(block_max)
    #
    #     # right[i]: maximum of nums[i] to block end
    #     block_max = nums[-1]
    #     for i in range(len(nums) - 1, -1, -1):
    #
    #         v = nums[i]
    #
    #         if i % k == k - 1:
    #             block_max = v
    #             right.append(v)
    #         else:
    #             if v > block_max:
    #                 right.append(v)
    #                 block_max = v
    #             else:
    #                 right.append(block_max)
    #     right.reverse()
    #
    #     # calc max_element
    #     for i in range(k - 1, len(nums)):
    #
    #         if i % k == k - 1:
    #             max_element.append(left[i])
    #         else:
    #             max_element.append(max(left[i], right[i - k + 1]))
    #
    #     return max_element


print(Solution().maxSlidingWindow([1, 2, 3, 4, 5], 3), [3, 4, 5])
print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5])
print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7])
