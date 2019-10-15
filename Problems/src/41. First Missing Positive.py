class Solution:
    """
    Given an unsorted integer array, find the smallest missing positive integer.
    Must be O(n) time, O(1) space.
    """


    def firstMissingPositive(self, nums) -> int:

        # empty case
        if not nums:
            return 1

        # not empty, sort first
        nums.sort()

        for i in range(len(nums)):

            # ignore when element not positive
            if nums[i] <= 0:
                continue

            # when start to encounter positive, check if there is missing
            else:

                # set last as zero
                last_num = 0

                # check from current positive num to the last to see if there is missing element
                for j in range(i, len(nums)):

                    # missing happens
                    if nums[j] - last_num > 1:
                        return last_num + 1

                    # no missing
                    else:

                        # no missing until the last element, return nums[-1] + 1
                        if j == len(nums) - 1:
                            return nums[j] + 1

                    # replace last num by current num
                    last_num = nums[j]

        # if all element are not positive, return 1
        return 1


print(Solution().firstMissingPositive([1, 2, 0]), 3)
print(Solution().firstMissingPositive([3, 4, -1, 1]), 2)
print(Solution().firstMissingPositive([7, 8, 10]), 1)
print(Solution().firstMissingPositive([-1, 1, 3]), 2)
