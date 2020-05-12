class Solution:
    """my sol, brute force, time n space n"""
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[-1][0]

    """my sol, bi-search, time logn, space 1"""
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if not nums:
            return None

        n = len(nums)
        i, j = 0, n - 1

        # bi-search
        while i < j:

            # take middle
            m = i + (j - i) // 2

            # check middle has two value - mark as middle left and middle right
            if m > 0 and nums[m - 1] == nums[m]:
                ml, mr = m - 1, m
            elif m < n - 1 and nums[m + 1] == nums[m]:
                ml, mr = m, m + 1
            else:
                return nums[m]

            # check whether single element is in left or right half
            if (j - mr) % 2 == 1:
                i = mr + 1
            else:
                j = ml - 1

        # answer
        return nums[i]
