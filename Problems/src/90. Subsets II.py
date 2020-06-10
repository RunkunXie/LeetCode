class Solution:

    """my dfs sol, modify from online and qishi sol"""
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()

        def dfs(path, idx):
            ans.append(path.copy())
            for i in range(idx, len(nums)):

                # handel dfs without visited, less easy to translate to other question
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                dfs(path + [nums[i]], i + 1)

        dfs([], 0)
        return ans

    """qishi dfs sol"""
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        visited = [False] * len(nums)

        def dfs(path, idx):
            ans.append(path.copy())

            for i in range(idx, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                dfs(path + [nums[i]], i + 1)
                visited[i] = False

        dfs([], 0)
        return ans

    """my iterative sol, 1st attempt"""
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]
        c = Counter(nums)

        for num, freq in c.items():
            new_set = []
            for f in range(1, freq + 1):
                new_set += [[num] * f + sub for sub in ans]
            ans += new_set

        return ans