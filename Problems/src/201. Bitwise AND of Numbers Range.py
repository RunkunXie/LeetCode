class Solution:
    """my sol, time 1, space 1"""
    #     def rangeBitwiseAnd(self, m: int, n: int) -> int:

    #         if m == n:
    #             return m

    #         if m == 0 or n == 0:
    #             return 0

    #         a = int(math.log2(m))
    #         b = int(math.log2(n))
    #         if b > a:
    #             return 0

    #         else:
    #             return 2 ** a + self.rangeBitwiseAnd(m - 2 ** a, n - 2 ** b)

    """ans - bit shift, time 1, space 1"""

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # find the common 1-bits
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift

    """ans - Brian Kernighan's algorithm, time 1, space 1"""

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            # turn off rightmost 1-bit
            n = n & (n - 1)
        return m & n
