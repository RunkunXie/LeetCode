class Solution:
    """my dp sol (state machine?), time 3*2*n = n"""
    def minCost(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        cur_costs = costs[0]

        for c in costs[1:]:
            cur_costs = [c[0] + min(cur_costs[1], cur_costs[2]),
                         c[1] + min(cur_costs[0], cur_costs[2]),
                         c[2] + min(cur_costs[0], cur_costs[1])]

        return min(cur_costs)