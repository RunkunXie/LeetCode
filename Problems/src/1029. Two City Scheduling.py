class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)
        costs = sorted(costs, key=lambda x: x[1] - x[0])
        return sum([c[1] for c in costs[:N // 2]]) + sum([c[0] for c in costs[N // 2:]])