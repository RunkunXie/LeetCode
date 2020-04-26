class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        total_sum = sum(cardPoints)
        n = len(cardPoints)

        if n <= k:
            return total_sum

        sum_len = n - k

        cur_sum = sum(cardPoints[:sum_len])
        min_sum = cur_sum

        for i in range(1, n - sum_len + 1):
            cur_sum = cur_sum - cardPoints[i - 1] + cardPoints[i + sum_len - 1]
            min_sum = min(cur_sum, min_sum)

        return total_sum - min_sum



