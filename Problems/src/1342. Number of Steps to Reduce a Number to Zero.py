class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            num, remainder = divmod(num, 2)
            count += 1 + remainder

        return count - 1
