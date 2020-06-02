class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """

    """note: Easy version of Q33"""
    """my sol, time log n"""
    def findMin(self, nums):
        # write your code here

        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= nums[end]:
                end = mid
            elif nums[mid] >= nums[start]:
                start = mid

        return nums[end] if nums[end] < nums[start] else nums[start]

