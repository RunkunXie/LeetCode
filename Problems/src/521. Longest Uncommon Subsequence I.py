class Solution:
    def findLUSlength(self, a: str, b: str) -> int:

        # m == n and a == b
        if a == b: return -1

        # (m != n) or (m == n and a != b)
        return max(len(a), len(b))
