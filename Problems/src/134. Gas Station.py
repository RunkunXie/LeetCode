class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        min_idx, min_val = 0, float("inf")
        cur_sum = 0
        n = len(gas)

        for i in range(n):
            cur_sum = cur_sum + gas[i] - cost[i]
            if cur_sum < min_val:
                min_val = cur_sum
                min_idx = i

        return (min_idx + 1) % n if sum(gas) - sum(cost) >= 0 else -1


