from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, idx in enumerate(index):
            ans.insert(nums[i], idx)

        return ans


print(Solution().createTargetArray(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1]))

