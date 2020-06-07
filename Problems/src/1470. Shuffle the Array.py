class Solution:
    """my sol time n"""
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i + n])

        return ans

    """online zip sol"""
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i, j in zip(nums[0:len(nums) // 2], nums[len(nums) // 2:]):
            res += [i, j]
        return res