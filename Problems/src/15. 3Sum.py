from typing import List


class Solution:
    """"""

    """my answer, time n^2"""
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #
    #     if len(nums) < 3:
    #         return None
    #
    #     nums = sorted(nums)
    #     if nums[0] > 0 or nums[-1] < 0:
    #         return None
    #
    #     ans_set = set()
    #     ans = []
    #     n = len(nums)
    #
    #     for i in range(n - 2):
    #
    #         if nums[i] > 0:
    #             break
    #
    #         l, r = i + 1, n - 1
    #
    #         while l != r:
    #             if nums[l] + nums[r] + nums[i] == 0:
    #                 if (nums[i], nums[l], nums[r]) not in ans_set:
    #                     ans.append([nums[i], nums[l], nums[r]])
    #                     ans_set.add((nums[i], nums[l], nums[r]))
    #                 l += 1
    #             elif nums[l] + nums[r] + nums[i] < 0:
    #                 l += 1
    #             else:
    #                 r -= 1
    #
    #     return ans

    """fast online answer, time n^2"""

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        zero_count = nums.count(0)
        if zero_count >= 3:
            res.append([0, 0, 0])
            [nums.remove(0) for _ in range(0, zero_count - 1)]

        nums = sorted(nums)
        pGroup, nGroup = [], []
        for n in nums:
            if n >= 0:
                pGroup.append(n)
            else:
                nGroup.append(n)
        nlen, plen = len(nGroup), len(pGroup)
        pSet, nSet = set(pGroup), set(nGroup)

        if len(nGroup) >= 2:
            previous_a = None
            for i in range(nlen - 1):
                a = nGroup[i]
                previous_b = None
                if previous_a == a:
                    continue

                for j in range(i + 1, nlen):
                    b = nGroup[j]
                    if previous_b == b:
                        continue

                    if -(a + b) in pSet:
                        res.append([-(a + b), a, b])
                    previous_b = b
                previous_a = a

        if len(pGroup) >= 2:
            previous_a = None
            for i in range(plen - 1):
                a = pGroup[i]
                previous_b = None
                if previous_a == a:
                    continue

                for j in range(i + 1, plen):
                    b = pGroup[j]
                    if previous_b == b:
                        continue

                    if -(a + b) in nSet:
                        res.append([-(a + b), a, b])
                    previous_b = b
                previous_a = a

        return res


print(Solution().threeSum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
