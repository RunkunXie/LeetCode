from typing import List


class Solution:
    """"""

    """my sol using start + 1 < end, 2nd attempt, time log n"""
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid

            # right half
            elif nums[mid] <= nums[end]:
                if nums[mid] <= target <= nums[end]:
                    start = mid
                else:
                    end = mid

            # left half
            elif nums[mid] >= nums[start]:
                if nums[start] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        return -1

    """my sol w/ hint, time logn"""
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        n = len(nums)
        l, r = 0, n - 1

        while l < r:

            mid = (l + r) // 2

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


