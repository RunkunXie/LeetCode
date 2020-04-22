# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    """my ans with hint, time n"""
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:

        m, n = binaryMatrix.dimensions()
        i, j = 0, n - 1
        ans = n

        while i < m and j >= 0:

            if binaryMatrix.get(i, j) == 0:
                i += 1
            else:
                ans = min(ans, j)
                j -= 1

        return ans if ans < n else -1
