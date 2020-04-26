class Solution:
    def maxScore(self, s: str) -> int:

        # ans
        max_score = 0

        # cum sum
        l_sum = 0
        r_sum = s.count('1')

        # update
        for char in s[:-1]:
            if char == '1':
                r_sum -= 1
            else:
                l_sum += 1
            max_score = max(l_sum + r_sum, max_score)

        return max_score

