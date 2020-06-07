class Solution:
    """my sol, 1st attempt, time nkk"""
    def minCostII(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        curr_cost = costs[0]

        for cost in costs[1:]:
            prev_cost = curr_cost.copy()
            for i in range(len(curr_cost)):
                curr_cost[i] = cost[i] + min(prev_cost[:i] + prev_cost[i + 1:])

        return min(curr_cost)

    """my sol, time nk"""
    def minCostII(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        curr_cost = costs[0]

        for cost in costs[1:]:
            prev_cost = curr_cost.copy()

            # find previous minimal, time k
            min_idx, minimal = 0, prev_cost[0]
            for i in range(1, len(prev_cost)):
                if prev_cost[i] < minimal:
                    min_idx, minimal = i, prev_cost[i]

            # update curr, time k
            curr_cost = [c + minimal for c in cost]

            # for min_idx, use 2nd minimal, time k
            curr_cost[min_idx] = cost[min_idx] + min(
                prev_cost[:min_idx] + prev_cost[min_idx + 1:])

        return min(curr_cost)

