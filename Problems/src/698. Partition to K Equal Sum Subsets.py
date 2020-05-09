class Solution:
    """ans, dfs, time k * 2**n"""
    # def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
    #
    #     target, rem = divmod(sum(nums), k)
    #     if rem: return False
    #
    #     def search(groups):
    #         if not nums: return True
    #         v = nums.pop()
    #         for i, group in enumerate(groups):
    #             if group + v <= target:
    #                 groups[i] += v
    #                 if search(groups): return True
    #                 groups[i] -= v
    #             if not group:
    #                 break  # game changer 2
    #         nums.append(v)
    #         return False
    #
    #     nums.sort()  # game changer 1
    #     if nums[-1] > target:
    #         return False
    #     while nums and nums[-1] == target:
    #         nums.pop()
    #         k -= 1
    #
    #     return search([0] * k)

    """online sol, dfs, better"""
    def canPartitionKSubsets(self, nums, k):
        nums.sort(reverse=True)  # Game Changer 1
        buck, kSum = [0] * k, sum(nums) // k

        def dfs(idx):
            if idx == len(nums): return len(set(buck)) == 1
            for i in range(k):
                buck[i] += nums[idx]
                if buck[i] <= kSum and dfs(idx + 1): return True
                buck[i] -= nums[idx]
                if buck[i] == 0: break  # Game Changer 2
            return False

        return dfs(0)

    """ans, dp + bit mask, time n * 2**n"""
    """learn the bit mask way!"""
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        target, rem = divmod(sum(nums), k)
        if rem or max(nums) > target: return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True

        def search(used, todo):
            if memo[used] is None:
                targ = (todo - 1) % target + 1
                memo[used] = any(search(used | (1 << i), todo - num)
                                 for i, num in enumerate(nums)
                                 if (used >> i) & 1 == 0 and num <= targ)
            return memo[used]

        return search(0, target * k)
