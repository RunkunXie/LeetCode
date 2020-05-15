class Solution:
    """my sol under hint"""
    def maxSubarraySumCircular(self, A: List[int]) -> int:

        n = len(A)
        A += A

        pref = []
        mono = deque([])
        ans = -float("inf")

        for i in range(n * 2):

            if i == 0:
                pref.append(A[0])
                mono.append(0)
                ans = max(ans, A[0])
                continue

            # prefix Sum
            pref.append(pref[-1] + A[i])

            # matain length of mono queue < n
            if mono and mono[0] < i - n:
                mono.popleft()

            # append answer before mono_queue push
            ans = max(ans, pref[i] - pref[mono[0]])

            # mono_queue push: pop + push
            # pop
            while mono and pref[i] <= pref[mono[-1]]:
                mono.pop()
            # push
            mono.append(i)

        return ans

    """online sol, modified Kadane's Algorithm - best one"""
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total, maxSum, curMax, minSum, curMin = 0, -float('inf'), 0, float('inf'), 0
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a

        # special case: all negative <=> maxSum < 0 <=> return max(A) = maxSum
        # in this case, total - minSum = 0, which is wrong
        return max(maxSum, total - minSum) if maxSum >= 0 else maxSum


