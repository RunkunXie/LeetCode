class Solution:
    """my sol under hint, monoqueue, time n"""
    def shortestSubarray(self, A: List[int], K: int) -> int:

        cur_sum = 0
        min_len = float("inf")

        # mono queue, (index, cur_sum)
        dq = deque([(-1, 0)])

        for i, num in enumerate(A):
            cur_sum += num

            # push
            while dq and dq[-1][1] > cur_sum:
                dq.pop()
            dq.append((i, cur_sum))

            # pop
            while dq and dq[-1][1] - dq[0][1] >= K:
                min_len = min(min_len, dq[-1][0] - dq[0][0])
                dq.popleft()

            if min_len == 1:
                return 1

        return min_len if min_len != float("inf") else -1

