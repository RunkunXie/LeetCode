class Solution:

    """my dfs sol, inspire by qishi, 1st attempt"""
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        visited = [False] * len(nums)

        def dfs(path, count):

            if count == len(nums):
                ans.append(path[:])  # copy the path
                return

            for i in range(len(nums)):
                if not visited[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                        continue
                    visited[i] = True
                    dfs(path + [nums[i]], count + 1)
                    visited[i] = False

        dfs([], 0)
        return ans
