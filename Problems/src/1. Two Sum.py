class Solution:
    def twoSum(self, nums, target: int):

        dict = {}

        for i, num in enumerate(nums):
            if num not in dict:
                dict[target - num] = i
            else:
                return [dict[num], i]