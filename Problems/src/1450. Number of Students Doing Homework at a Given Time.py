"""Weekly Contest 189 - Q1"""


class Solution:
    """my sol"""
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:

        ans = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                ans += 1

        return ans
