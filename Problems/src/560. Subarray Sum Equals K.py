class Solution:
    """my sol, time n^2"""
    #     def subarraySum(self, nums: List[int], k: int) -> int:

    #         ans = 0
    #         for i in range(len(nums)):
    #             cur_sum = 0
    #             for j in range(i, len(nums)):
    #                 cur_sum += nums[j]
    #                 if cur_sum == k:
    #                     ans += 1
    #         return ans

    """online sol, time n"""

    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        sum_dict = defaultdict(int)

        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum == k:
                ans += 1
            if cur_sum - k in sum_dict:
                ans += sum_dict[cur_sum - k]
            sum_dict[cur_sum] += 1

        return ans