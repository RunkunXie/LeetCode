from typing import List


class Solution:

    """my sol under ans, 2nd attempt"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        def twoSum(num, i):
            start, end = i, len(nums) - 1
            while start < end:
                cur = nums[start] + nums[end] + num
                if cur < 0:
                    start += 1
                elif cur > 0:
                    end -= 1
                elif start > i and nums[start] == nums[start - 1]:
                    start += 1
                elif end < len(nums) - 1 and nums[end] == nums[end + 1]:
                    end -= 1
                else:
                    ans.append([num, nums[start], nums[end]])
                    start += 1
                    end -= 1

        for i, num in enumerate(nums):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i - 1]:
                twoSum(num, i + 1)

        return ans

    """my sol, 2nd attempt, slow"""
    from bisect import bisect_left, bisect
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:

            nums.sort()
            ans, cur_sum, left_zero, right_zero = [], 0, bisect_left(nums, 0), bisect(nums, 0)
            neg_set, pos_set = set(nums[:left_zero]), set(nums[right_zero:])
            num_zeros = right_zero - left_zero

            for n in neg_set:
                start, end = right_zero, len(nums) - 1
                while start < end:
                    cur_sum = nums[start] + nums[end] + n
                    if start > 0 and nums[start] == nums[start - 1]:
                        start += 1
                    elif end < len(nums) - 1 and nums[end] == nums[end + 1]:
                        end -= 1
                    elif cur_sum == 0:
                        ans.append([n, nums[start], nums[end]])
                        start += 1
                        end -= 1
                    elif cur_sum < 0:
                        start += 1
                    elif cur_sum > 0:
                        end -= 1

                if num_zeros and -n in pos_set:
                    ans.append([n, 0, -n])

            for p in pos_set:
                start, end = 0, left_zero - 1
                while start < end:
                    cur_sum = nums[start] + nums[end] + p
                    if start > 0 and nums[start] == nums[start - 1]:
                        start += 1
                    elif end < len(nums) - 1 and nums[end] == nums[end + 1]:
                        end -= 1
                    elif cur_sum == 0:
                        ans.append([nums[start], nums[end], p])
                        start += 1
                        end -= 1
                    elif cur_sum < 0:
                        start += 1
                    elif cur_sum > 0:
                        end -= 1

            if num_zeros >= 3:
                ans.append([0, 0, 0])

            return ans

    """ans, time n^2"""
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            cur_sum = nums[i] + nums[lo] + nums[hi]
            if cur_sum < 0 or (lo > i + 1 and nums[lo] == nums[lo - 1]):
                lo += 1
            elif cur_sum > 0 or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1

    """my sol, 1st attempt, time n^2"""
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
