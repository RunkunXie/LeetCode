class Solution:
    """my sol, time logn + 2log(n/2)"""
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # corner
        if not nums:
            return [-1, -1]

        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        # init
        n = len(nums)
        i, j = 0, n - 1
        m = (i + j) // 2

        # bisearch
        while i < j:

            if nums[m] == target:
                break
            elif nums[m] < target:
                i = m + 1
            else:
                j = m - 1

            m = (i + j) // 2

        # if not find
        if nums[m] != target:
            return [-1, -1]

        # if find
        l = r = m

        while i < l - 1:
            m = (i + l) // 2

            if nums[m] == target:
                l = m
            else:
                i = m + 1

        if nums[i] == target:
            l = i

        while j > r + 1:
            m = (r + j) // 2

            if nums[m] == target:
                r = m
            else:
                j = m - 1

        if nums[j] == target:
            r = j

        return [l, r]


class Solution:
    """online bisearch sol, time 2logn"""
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearchLeft(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(A, x):
            left, right = 0, len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if x >= A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left, right = binarySearchLeft(nums, target), binarySearchRight(nums, target)
        return (left, right) if left <= right else [-1, -1]

