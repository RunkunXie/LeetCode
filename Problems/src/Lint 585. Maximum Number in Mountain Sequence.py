class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    """
        equivalent: LC Q852
        follow up: LC Q1095
    """

    """my recursive sol"""
    # def mountainSequence(self, nums):
    #     # write your code here
    #
    #     if not nums:
    #         return -1
    #
    #     start = 0
    #     end = len(nums) - 1
    #
    #     while start + 1 < end:
    #         mid = start + (end - start) // 2
    #         if nums[mid] <= nums[end]:
    #             start = mid
    #         elif nums[mid] <= nums[start]:
    #             end = mid
    #         else:
    #             return max(self.mountainSequence(nums[:mid]),
    #                        self.mountainSequence(nums[mid:]))
    #
    #     return max(nums[start], nums[end])

    """my sol under hint, binary search"""
    def mountainSequence(self, nums):
        # write your code here

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

        return max(nums[start], nums[end])