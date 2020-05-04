class Solution:
    """my sol, time nlogn"""
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)

        ans = []

        for i in intervals:

            if not ans:
                ans.append(i)
                continue

            if i[0] <= ans[-1][1]:
                last = ans.pop()
                ans.append([last[0], max(last[1], i[1])])
            else:
                ans.append(i)

        return ans
