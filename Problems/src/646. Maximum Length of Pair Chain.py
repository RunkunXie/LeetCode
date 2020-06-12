class Solution:

    """greedy ans, time nlogn"""
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        ans, prev = 0, -float("inf")
        for x, y in sorted(pairs, key=lambda x: x[1]):
            if x > prev:
                ans += 1
                prev = y
        return ans

    """my dp bisect sol, 1st attempt, time nlogn"""
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()
        tails = []
        for p in pairs:
            i = bisect_left([t[1] for t in tails], p[0])
            if i == len(tails):
                tails.append(p)
            else:
                if p[1] < tails[i][1]:
                    tails[i] = p

        return len(tails)

    """my dp sol, 1st attempt, time n^2"""
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort()
        dp = [1] * len(pairs)

        for j in range(1, len(pairs)):
            for i in range(j):
                if pairs[j][0] > pairs[i][1]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp) if pairs else 0


