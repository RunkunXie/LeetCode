from typing import List


class Solution:
    """"""

    """my sol, time n"""
    # def search(self, nums: List[int], target: int) -> int:
    #
    #     i = 0
    #     for i, num in enumerate(nums):
    #         if num == target:
    #             return i
    #
    #     return -1

    """my sol w/ hint, time logn"""
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        n = len(nums)
        l, r = 0, n - 1

        while l < r:

            mid = (l + r) // 2
            print(l, r, mid)

            if nums[mid] == target:
                return mid

            # left half increasing
            elif nums[mid] >= nums[l]:
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            # right half increasing
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return l if nums[l] == target else -1


