class Solution:
    """my sol under hint, counting sort, time 2n, space 3"""
    #     def sortColors(self, nums: List[int]) -> None:
    #         """
    #         Do not return anything, modify nums in-place instead.
    #         """

    #         count = defaultdict(int)
    #         for num in nums:
    #             count[num] += 1

    #         i = 0
    #         for c in range(3):
    #             while count[c] > 0:
    #                 nums[i] = c
    #                 i += 1
    #                 count[c] -= 1

    """ans, time 1n, space 1"""
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1

