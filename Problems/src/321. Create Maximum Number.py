class Solution:
    """my sol under hint - first attempt, time k * (m + n) * (m + n)"""
    # def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
    #
    #     m, n = len(nums1), len(nums2)
    #     ans = None
    #
    #     # iterate k
    #     for i in range(k + 1):
    #         len1, len2 = i, k - i
    #         if len1 <= m and len2 <= n:
    #
    #             # time m + n
    #             l1 = self.largestKdigits(nums1, len1)
    #             l2 = self.largestKdigits(nums2, len2)
    #
    #             # average time m + n, worst case (m + n) ^ 2
    #             cur_ans = self.mergeTwoList(l1, l2)
    #
    #             if not ans:
    #                 ans = cur_ans
    #             else:
    #                 if self.compareTwoEqualLenList(cur_ans, ans):
    #                     ans = cur_ans
    #
    #     return ans
    #
    # @staticmethod
    # def mergeTwoList(l1, l2):
    #
    #     return [max(l1, l2).pop(0) for _ in l1 + l2]
    #
    # @staticmethod
    # def compareTwoEqualLenList(l1, l2):
    #
    #     for i in range(len(l1)):
    #         if l1[i] > l2[i]:
    #             return True
    #         elif l1[i] < l2[i]:
    #             return False
    #
    #     return True
    #
    # @staticmethod
    # def largestKdigits(nums, k):
    #
    #     remove_num = len(nums) - k
    #     mono_q = []
    #
    #     for i in nums:
    #         while remove_num > 0 and mono_q and mono_q[-1] < i:
    #             mono_q.pop()
    #             remove_num -= 1
    #         mono_q.append(i)
    #
    #     mono_q = mono_q[:-remove_num] if remove_num > 0 else mono_q
    #
    #     return mono_q
    pass


class Solution:
    """my modified sol - based on online sol, time k * (m + n) * (m + n)"""
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        return max(self.mergeTwoList(self.largestKdigits(nums1, i),
                                     self.largestKdigits(nums2, k - i))
                   for i in range(k + 1)
                   if i <= len(nums1) and k - i <= len(nums2))

    @staticmethod
    def mergeTwoList(l1, l2):

        return [max(l1, l2).pop(0) for _ in l1 + l2]

    @staticmethod
    def largestKdigits(nums, k):

        remove_num = len(nums) - k
        mono_q = []

        for i in nums:
            while remove_num > 0 and mono_q and mono_q[-1] < i:
                mono_q.pop()
                remove_num -= 1
            mono_q.append(i)

        mono_q = mono_q[:-remove_num] if remove_num > 0 else mono_q

        return mono_q




