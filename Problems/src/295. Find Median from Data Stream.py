# class MedianFinder:
#     """
#     binary sorted search, searchO(logN), insert O(N), exceed limit
#     """
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.val = []
#         self.len = 0
#
#     def _find_i(self, num):
#
#         l = 0
#         r = self.len - 1
#
#         if self.val[l] >= num:
#             return l
#         elif self.val[r] <= num:
#             return r + 1
#
#         while r - l > 1:
#             m = int((l + r) / 2)
#
#             if self.val[m] > num:
#                 r = m
#             elif self.val[m] < num:
#                 l = m
#             else:
#                 return m
#
#         return r
#
#     def addNum(self, num: int) -> None:
#         """
#
#         :param num:
#         :return:
#         """
#
#         if self.val:
#             if num is not None:
#                 i = self._find_i(num)
#                 self.val = self.val[:i] + [num] + self.val[i:]
#                 self.len += 1
#                 return None
#         else:
#             if num is not None:
#                 self.val.append(num)
#                 self.len += 1
#
#     def findMedian(self) -> float:
#
#         if self.len == 0:
#             return None
#         elif self.len % 2 == 0:
#             return (self.val[int(self.len / 2) - 1] + self.val[int(self.len / 2)]) / 2
#         else:
#             return self.val[int(self.len / 2)]

from heapq import *


class MedianFinder:
    """
    using two heap, insert 2 * O(logN), find O(1), beat 90%
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lo = []
        self.hi = []
        self.len = 0

    def addNum(self, num: int) -> None:
        """

        :param num:
        :return:
        """
        if num is not None:
            if self.lo:
                max_lo = - self.lo[0]
                if num > max_lo:
                    heappush(self.hi, num)
                else:
                    heappush(self.lo, - num)
            else:
                heappush(self.lo, - num)
            self.len += 1

        if len(self.lo) - len(self.hi) > 1:
            heappush(self.hi, - heappop(self.lo))
        elif len(self.lo) < len(self.hi):
            heappush(self.lo, - heappop(self.hi))

    def findMedian(self) -> float:

        if self.len == 0:
            return None
        elif self.len % 2 == 0:
            return (self.hi[0] - self.lo[0]) / 2
        else:
            return - self.lo[0]


# Your MedianFinder object will be instantiated and called as such:
print("\n case 1")
obj = MedianFinder()
lists = [None, None, 1, None, 2, 3, 6, 2]
for v in lists:
    obj.addNum(v)
    print(obj.findMedian(), end=' ')

print("\n case 2")
obj = MedianFinder()
lists = [None, 0, 0, None]
for v in lists:
    obj.addNum(v)
    print(obj.findMedian(), end=' ')

print("\n case 3")
obj = MedianFinder()
lists = [6, 10, 2, 6, 5, 0]
for v in lists:
    obj.addNum(v)
    print(obj.findMedian(), end=' ')
