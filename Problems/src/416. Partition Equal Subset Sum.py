class Solution:
    """my sol, time n^2"""
    def canPartition(self, nums) -> bool:

        if not nums:
            return False

        if sum(nums) % 2:
            return False

        target = sum(nums) / 2
        available = {0}

        for num in nums:
            for cur in list(available):
                if cur + num not in available:
                    available.add(cur + num)
            if target in available:
                return True

        return False

