class Solution:
    """"""

    """use hash map - dictionary, time n, space n"""
    # def findDisappearedNumbers(self, nums):
    #
    #     dict = {_: _ for _ in range(1, len(nums) + 1)}
    #
    #     for num in nums:
    #         dict[num] = 0
    #
    #     ans = []
    #     for v in dict.values():
    #         if v > 0: ans.append(v)
    #
    #     return ans


    """use hash map - set, one-line code, time n, space n"""
    # def findDisappearedNumbers(self, nums):
    #
    #     return list(set(range(1,len(nums)+1))-set(nums))

    """inplace, time n, space 1"""
    def findDisappearedNumbers(self, nums):

        for i in range(len(nums)):
            loc = abs(nums[i]) - 1
            nums[loc] = -abs(nums[loc])

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0: ans.append(i + 1)

        return ans