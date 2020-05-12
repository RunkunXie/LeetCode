class Solution:
    """my sol under hint, time n, space 1, in place"""
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n > 1:

            idx = n - 1

            # find idx
            while idx > 0:
                if nums[idx - 1] < nums[idx]:
                    break
                idx -= 1

            # corner case
            if idx == 0:
                nums.reverse()

            else:
                # find maximum idx_l from nums[idx:], where nums[idx_l] > nums[idx - 1]
                idx_l = idx
                for i in range(idx, n):
                    if nums[i] > nums[idx - 1]:
                        idx_l = max(idx_l, i)

                # swap, and reverse
                nums[idx - 1], nums[idx_l] = nums[idx_l], nums[idx - 1]
                nums[idx:] = reversed(nums[idx:])




