# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        if isBadVersion(1):
            return 1

        def binarySearch(l, r):

            if l + 1 == r:
                return r

            m = int((l + r) / 2)
            if isBadVersion(m):
                return binarySearch(l, m)
            else:
                return binarySearch(m, r)

        return binarySearch(1, n)