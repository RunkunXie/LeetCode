from typing import List


class Solution:
    """"""

    """my recursive sol, 2nd attempt"""
    def permute(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return [[]]

        ans = []
        for i in range(len(nums)):
            sub = self.permute(nums[:i] + nums[i + 1:])
            ans += [[nums[i]] + s for s in sub]

        return ans

    """my dfs sol, 2nd attempt"""
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        visited = [False] * len(nums)

        def dfs(path, count):

            if count == len(nums):
                ans.append(path[:])  # copy the path
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dfs(path + [nums[i]], count + 1)
                    visited[i] = False

        dfs([], 0)
        return ans

    """online solution, recursion"""
    def permute(self, nums: List[int]) -> List[List[int]]:

        if len(nums) == 1:
            return [nums]
        result = []
        for i in range(len(nums)):
            others = nums[:i] + nums[i + 1:]
            other_permutations = self.permute(others)
            for permutation in other_permutations:
                result.append([nums[i]] + permutation)
        return result

    """solution, backtracking"""
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # if all integers are used up
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output