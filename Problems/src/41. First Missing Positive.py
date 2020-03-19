class Solution:
    """
    Given an unsorted integer array, find the smallest missing positive integer.
    Must be O(n) time, O(1) space.
    """

    # def firstMissingPositive(self, nums) -> int:
    #     """
    #     sort takes O(nlogn)
    #     :param nums:
    #     :return:
    #     """
    #     # empty case
    #     if not nums:
    #         return 1
    #
    #     # not empty, sort first
    #     nums.sort()
    #
    #     for i in range(len(nums)):
    #
    #         # ignore when element not positive
    #         if nums[i] <= 0:
    #             continue
    #
    #         # when start to encounter positive, check if there is missing
    #         else:
    #
    #             # set last as zero
    #             last_num = 0
    #
    #             # check from current positive num to the last to see if there is missing element
    #             for j in range(i, len(nums)):
    #
    #                 # missing happens
    #                 if nums[j] - last_num > 1:
    #                     return last_num + 1
    #
    #                 # no missing
    #                 else:
    #
    #                     # no missing until the last element, return nums[-1] + 1
    #                     if j == len(nums) - 1:
    #                         return nums[j] + 1
    #
    #                 # replace last num by current num
    #                 last_num = nums[j]
    #
    #     # if all element are not positive, return 1
    #     return 1

    # def firstMissingPositive(self, nums) -> int:
    #     """
    #      takes O(n) time, O(n) extra space
    #     :param nums:
    #     :return:
    #     """
    #     # empty case
    #     if not nums:
    #         return 1
    #
    #     # find max
    #     max_num = nums[0]
    #     for num in nums:
    #         if num > max_num:
    #             max_num = num
    #
    #     if max_num <= 0:
    #         return 1
    #
    #     # dict
    #     dict = {_:0 for _ in range(1, max_num + 1)}
    #     for num in nums:
    #         if num > 0:
    #             dict[num] += 1
    #
    #     for k, v in dict.items():
    #         if v == 0:
    #             return k
    #
    #     return k + 1

    def firstMissingPositive(self, nums) -> int:
        """
         takes O(n) time, O(1) extra space
        :param nums:
        :return:
        """
        # # empty case
        # if not nums:
        #     return 1

        # best solution
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i

        return n


print(Solution().firstMissingPositive([1, 2, 0]), 3)
print(Solution().firstMissingPositive([3, 4, -1, 1]), 2)
print(Solution().firstMissingPositive([7, 8, 10]), 1)
print(Solution().firstMissingPositive([-1, 1, 3]), 2)
print(Solution().firstMissingPositive([1]), 2)
