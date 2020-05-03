class Solution:
    """my sol, time nlogn"""
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n, s1, s2 = len(s1), sorted(s1), sorted(s2)

        return all([s1[i] >= s2[i] for i in range(n)]) or all([s1[i] <= s2[i] for i in range(n)])


class Solution:
    """online time n sol"""
    def check(self, d1, d2):
        s = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            s += d1[c] - d2[c]
            if s < 0:
                return False
        return True

    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)
        return self.check(d1, d2) | self.check(d2, d1)