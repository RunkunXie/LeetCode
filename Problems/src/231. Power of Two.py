class Solution:
    """my sol, time log n"""
    def isPowerOfTwo(self, n: int) -> bool:
        prev, curr, i = 0, 1, 0

        while curr < n:
            prev = curr
            curr *= 2

        return n == curr

    """ans, time 1"""
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (n - 1) == 0  # Turn off the Rightmost 1-bit
        # return n & (-n) == n  # Get the Rightmost 1-bit
