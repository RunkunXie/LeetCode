class Solution:
    """my deque sol, time n"""
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

        # init dq and answer
        dq = collections.deque([(0, nums[0])])
        ans = nums[0]

        for i in range(1, len(nums)):

            # new element
            new_sum = max(dq[0][1], 0) + nums[i]

            # push new element
            while dq and dq[-1][1] < new_sum:
                dq.pop()
            dq.append((i, new_sum))

            # check condition k
            if i - dq[0][0] >= k:
                dq.popleft()

            # update answer
            ans = max(ans, dq[0][1])

        return ans

    """online deque sol, time n"""
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        d = collections.deque([(0, nums[0])])
        ans = nums[0]
        for i in range(1, len(nums)):
            idx, lastKSumMax = d[0]
            if idx == i - k:
                d.popleft()
            newSum = max(lastKSumMax, 0) + nums[i]
            ans = max(ans, newSum)
            while d and d[-1][1] < newSum:
                d.pop()
            d.append((i, newSum))
        return ans

    """my sol, time limit exceeded"""
#     def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

#         n = len(nums)

#         ans = max(nums)
#         if ans < 0:
#             return ans

#         sm = [[0] * (k + 1) for _ in range(n + 1)]

#         for i in range(1, k + 1):
#             sm[0][i] = - float("inf")

#         ans = nums[0]

#         for i in range(1, n + 1):

#             num = nums[i - 1]

#             sm[i][1] = max(sm[i - 1][1:] + [0]) + num

#             if k >= 2:
#                 for j in range(2, k + 1):
#                     sm[i][j] = sm[i - 1][j - 1]

#             ans = max(ans, sm[i][1])

#         return ans




