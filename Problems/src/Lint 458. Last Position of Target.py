class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    """my sol using start < end, time log n"""
    def lastPosition(self, nums, target):
        # write your code here

        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid

        if nums[start] == target:
            return start
        elif start - 1 >= 0 and nums[start - 1] == target:
            return start - 1

        return -1

    """my sol using start + 1 < end, time log n"""
    def lastPosition(self, nums, target):
        # write your code here

        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start

        return -1