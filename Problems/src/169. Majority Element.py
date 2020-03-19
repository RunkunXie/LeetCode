class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        major = len(nums) / 2
        freq = {}

        for num in nums:

            if freq.get(num):
                freq[num] += 1
            else:
                freq[num] = 1

            if freq[num] >= major:
                return num