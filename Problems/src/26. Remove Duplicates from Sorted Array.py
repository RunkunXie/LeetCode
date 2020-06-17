class Solution:
    """my 1st attempt sol"""
    def removeDuplicates(self, nums: List[int]) -> int:

        start = -1

        for i in range(len(nums)):

            if i == len(nums) - 1 or nums[i] != nums[i + 1]:
                start += 1
                nums[start], nums[i] = nums[i], nums[start]

        nums[:] = nums[:start + 1]
