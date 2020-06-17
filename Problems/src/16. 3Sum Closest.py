class Solution:
    """my sol, 1st attempt"""
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        self.diff = float("inf")
        nums.sort()

        def twoSum(start, end, target):

            while start < end:
                diff = nums[start] + nums[end] - target
                if abs(diff) < abs(self.diff):
                    self.diff = diff

                if diff > 0:
                    end -= 1
                elif diff < 0:
                    start += 1
                else:
                    return

        for i in range(len(nums) - 2):
            twoSum(i + 1, len(nums) - 1, target - nums[i])

        return target + self.diff
