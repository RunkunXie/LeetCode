class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        nums = A
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid - 1]:
                start = mid
            else:
                end = mid

        return start if nums[start] > nums[end] else end